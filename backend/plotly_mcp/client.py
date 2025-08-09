"""The Charting Client - an Agent"""
import json
import logging
from typing import List

from fastmcp import Client
from fastmcp.client.transports import FastMCPTransport
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

from dotenv import load_dotenv

from .plotly_mcp import plotly_mcp
from .input_schema import OpenAiMessage

load_dotenv(override=True)

logger = logging.getLogger(__name__)

from config import config

class ChartBot:
    def __init__(self):
        transport = FastMCPTransport(plotly_mcp)
        self.mcp = Client(transport=transport)
        print(config.llm.connection_params)
        print(config.llm.MODEL)
        self.llm = OpenAI(**config.llm.connection_params)
        self.model = config.llm.MODEL 

    @property
    def basic_system_prompt(self) -> List[OpenAiMessage]:
        """Returns a message containing the base system prompt for charting"""
        return [
            {
                "role": "system",
                "content": "You are an expert in data visualisation that can generate charts based on user requests. Use the available tools to complete the request. For some queries you may need to call multiple tools to get the final result.",
            },
        ]
    
    @property
    def personality_prompt(self) -> List[OpenAiMessage]:
        """Return a 'personality' for the bot"""
        return [
            {
                "role":"system",
                "content":"You should always reply in the style of Thomas Malory, but don't be too verbose"
            },
        ]

    async def run(self, message_stream:list):
        """Process the message chain, run selected tools, and return all outputs"""

        # If the message stream contains only the initial user prompt, add the system prompt
        if len(message_stream) == 1:
            messages = self.basic_system_prompt
        else:
            messages = []

        messages += self.personality_prompt + message_stream

        try:
            async with self.mcp as session:
                response = await session.list_tools()
            available_tools = [
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.inputSchema,
                    },
                }
                for tool in response
            ]

        except Exception as e:
            return f"Error connecting to MCP server: {str(e)}"

        # Initial Claude API call
        response = self.llm.chat.completions.create(
            model=self.model,
            max_tokens=1000,
            temperature=0,
            messages=messages,
            tools=available_tools,
        )

        output = [*message_stream]
        current_message = response.choices[0].message

        # Continue processing while there are tool calls
        if current_message.tool_calls:
            if current_message.content:
                output.append({
                    "role":current_message.role,
                    "content":current_message.content
                })

            # Add the assistant's message with tool calls to conversation
            messages.append(
                {
                    "role": "assistant",
                    "content": current_message.content,
                    "tool_calls": [
                        {
                            "id": tool_call.id,
                            "type": "function",
                            "function": {
                                "name": tool_call.function.name,
                                "arguments": tool_call.function.arguments,
                            },
                        }
                        for tool_call in current_message.tool_calls
                    ],
                }
            )

            # Execute each tool call and add results
            for tool_call in current_message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                try:
                    # Execute tool call
                    async with self.mcp as session:
                        result = await session.call_tool(tool_name, tool_args)
                    output.append({
                        "role":"chart",
                        "content":result.data
                    })
                except Exception as e:
                    result = type(
                        "Result",
                        (),
                        {"content": f"Error calling tool {tool_name}: {str(e)}"},
                    )()

                

                # Add tool result to messages in OpenAI format
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result.content)
                        if hasattr(result, "content")
                        else str(result),
                    }
                )

            # Get next response from Databricks
            response = self.llm.chat.completions.create(
                model=self.model,
                max_tokens=1000,
                temperature=0,
                messages=messages,
                tools=available_tools,
            )

            current_message = response.choices[0].message

        # Add final response if it has content
        if current_message.content:
            output.append({
                "role":current_message.role,
                "content":current_message.content
            })

        return output
