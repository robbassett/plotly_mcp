"""Global Config Settings for Backend"""
import os
from functools import lru_cache
from typing import Dict
from pydantic_settings import BaseSettings
from pydantic import field_validator
import dotenv

# Load env vars
dotenv.load_dotenv()

class LlmConfig(BaseSettings):
    """Configuration for LLM"""
    BASE_URL: str = os.environ.get("OPENAI_API_KEY","")
    TOKEN: str = os.environ.get("OPENAI_API_TOKEN","")

    @property
    def connection_params(self) -> Dict[str,str]:
        """Return the LLM connection params"""
        return {
            "base_url":self.BASE_URL,
            "api_token":self.TOKEN
        }
    
class APIConfig(BaseSettings):
    """Config for FastAPI"""
    TITLE: str = "Dummy API for Plotly MCP Demo"
    DESCRIPTION: str = """
    This is a dummy API that contains very little of value, but is simply used to demonstrate
    how to mount a FastMCP server to a FastAPI application, connect a custom chatbot interface
    to an API endpoint, and connect that API endpoint to a LLM utilising your MCP server. It's
    and all in one package!
    """
    SUMMARY: str = "Dummy FastAPI for MCP Demo"
    VERSION: str = "0.0.0"

class LogConfig(BaseSettings):
    """Configuration for application logging."""
    LEVEL: str = "INFO"
    FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    FILE_PATH: str = "plotly_mcp.log"
    
class Settings(BaseSettings):
    """Main Settings"""
    llm: LlmConfig = LlmConfig()
    api: APIConfig = APIConfig()
    log: LogConfig = LogConfig()

@lru_cache()
def get_settings() -> Settings:
    """Get cached application settings."""
    return Settings()


# For importing to other modules
config = get_settings()
