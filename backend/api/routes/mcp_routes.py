"""Router for chatbot"""
from fastapi import APIRouter, Depends, Body
from typing import Annotated
import logging

from api.service.mcp_service import McpService
from . import schema

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/chat"
)

def get_service():
    """Dependency to get the Chatbot service instance."""
    return McpService()

@router.post("/query")
async def run_query(
    payload: Annotated[
        schema.OpenAiQuery,
        Body(
            examples=[
                {
                    "messages":[
                        {
                            "content":"I want to make a chart of fun as a function of time, time is in days and covers day 0 to day 15, and fun starts at one and increases by the day number each day!"
                        }
                    ]
                }
            ]
        )
    ],
    service: McpService = Depends(get_service)
):
    return await service.process_query(payload.messages)