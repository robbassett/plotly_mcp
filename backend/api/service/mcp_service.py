"""
service layer for chatbot
"""
from typing import Optional, List

from api.repository.mcp_repository import McpRepository
from plotly_mcp.input_schema import OpenAiMessage

class McpService:
    """Service for MCP Chatbot"""

    def __init__(self, repository: Optional[McpRepository] = None) -> None:
        """Initialise the service"""
        self.repository = repository or McpRepository()

    async def process_query(self, message_stream: List[OpenAiMessage]):
        _llm_input = [
            {"role":message.role,"content":message.content}
            for message in message_stream
        ]
        try:
            return await self.repository.process_messages(_llm_input)
        except Exception as e:
            return {"error":str(e)}
