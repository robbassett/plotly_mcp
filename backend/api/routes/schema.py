from typing import List
from pydantic import BaseModel

class OpenAiMessage(BaseModel):
    role: str = 'user'
    content: str

class OpenAiQuery(BaseModel):
    messages: List[OpenAiMessage]
