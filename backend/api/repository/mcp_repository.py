"""Repository for using MCP server"""
from typing import Optional, Dict
import os
import asyncio

from plotly_mcp.client import ChartBot

class McpRepository:
    def __init__(self) -> None:
        self.fullfiller = ChartBot()

    async def process_messages(self,messages: list):
        return await self.fullfiller.run(messages)
