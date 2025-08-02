"""Main script containing the FastAPI application to which the MCP and React Frontend are Mounted"""
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from config import config
from plotly_mcp import plotly_mcp

# Configure logging
logging.basicConfig(
    level=getattr(logging, config.log.LEVEL),
    format=config.log.FORMAT,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(config.log.FILE_PATH)
    ]
)
logger = logging.getLogger(__name__)

# Import routers

# Load MCP here to allow the lifespan to be included in the FastAPI application
mcp_app = plotly_mcp.http_app(path="/mcp")

# Remake the app to ensure the lifespan matches the MCP server,
# this is required as we want to co-host the API and MCP
app = FastAPI(
    title=config.api.TITLE,
    description=config.api.DESCRIPTION,
    summary=config.api.SUMMARY,
    version=config.api.VERSION,
    lifespan=mcp_app.lifespan
)

# Include routers
#app.include_router(placeholder)

# Add MCP server
app.mount("/", mcp_app)

# Adding CORS middleware to allow frontend to access when running dev locally
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add frontend - serve static files for all assets
# app.mount("/assets", StaticFiles(directory="frontend/assets"), name="assets")

# @app.get("/")
# async def serve_spa_root():
#     return FileResponse("frontend/index.html")
