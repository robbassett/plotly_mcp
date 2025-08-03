# Plotly MCP Demo

A comprehensive demonstration of creating a complex charting Model Context Protocol (MCP) server integrated with a FastAPI application and React frontend. This project showcases how to build a complete chat-based data visualization system where AI chatbots can generate interactive Plotly charts through MCP tools.

## ⚠️ Important Note

**This is NOT an installable module.** This project is designed as a demonstration and reference implementation for building MCP-enabled applications. It shows how to integrate multiple technologies into a cohesive system for AI-powered data visualization.

## 🏗️ Architecture Overview

This project demonstrates a three-tier architecture:

1. **MCP Server** (`backend/plotly_mcp/`) - Provides chart generation tools via Model Context Protocol
2. **FastAPI Backend** (`backend/`) - Serves the MCP server and provides chat API endpoints
3. **React Frontend** (`frontend/`) - Chat interface for interacting with the AI and viewing charts

All three components are designed to be served from a single FastAPI application, creating a unified deployment model.

## 🎯 Project Purpose

This demonstration shows how to:

- Create a sophisticated MCP server with multiple chart generation tools
- Integrate MCP servers with FastAPI applications
- Build chat interfaces that can leverage MCP tools for data visualization
- Serve multiple application components from a single FastAPI instance
- Enable AI chatbots to generate interactive charts through natural language

## 🚀 Current Features

### MCP Server (Plotly Tools)
- **Line Charts**: Multi-trace line plots with customizable labels and axes
- **Bar Charts**: Category-based bar visualizations
- **Heat Maps**: 2D intensity visualizations with color mapping
- JSON-based chart output compatible with Plotly.js

### FastAPI Backend
- MCP server hosting at `/mcp` endpoint
- Chat API at `/chat/query` for processing natural language requests
- CORS configuration for local development
- Structured logging and configuration management

### React Frontend (ChartChat)
- Modern React 19 with TypeScript
- Chakra UI component library
- Plotly.js integration for chart rendering
- Chat interface components for AI interaction
- Axios-based API communication

## 📁 Project Structure

```
plotly_mcp/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py              # Application configuration
│   ├── requirements.txt       # Python dependencies
│   ├── api/
│   │   ├── routes/
│   │   │   ├── mcp_routes.py  # Chat API endpoints
│   │   │   └── schema.py      # API schemas
│   │   ├── service/
│   │   │   └── mcp_service.py # Chat processing service
│   │   └── repository/
│   │       └── mcp_repository.py # Data access layer
│   └── plotly_mcp/
│       ├── plotly_mcp.py      # MCP server implementation
│       ├── client.py          # MCP client utilities
│       └── input_schema.py    # Chart input schemas
├── frontend/
│   ├── src/
│   │   ├── Components/
│   │   │   ├── ChatMessage.tsx
│   │   │   └── ChatStream.tsx
│   │   ├── Interfaces/
│   │   │   └── ChatInterface.ts
│   │   ├── api/
│   │   │   └── endpoints.ts
│   │   └── App.tsx
│   ├── package.json
│   └── vite.config.ts
└── README.md
```

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **FastMCP** - MCP server implementation
- **Plotly** - Chart generation library
- **Pydantic** - Data validation and settings
- **OpenAI** - AI model integration

### Frontend
- **React 19** - Modern React with TypeScript
- **Vite** - Fast build tool and dev server
- **Chakra UI** - Component library
- **Plotly.js** - Interactive chart rendering
- **Axios** - HTTP client

## 🚧 Current Status & Roadmap

### ✅ Completed
- [x] Basic MCP server with three chart types (line, bar, heatmap)
- [x] FastAPI application structure with MCP integration
- [x] React frontend with chat interface components
- [x] API endpoints for chat processing
- [x] CORS configuration for local development

### 🔄 In Progress / TODO

#### 1. Frontend Integration
- [ ] Mount React frontend to FastAPI application
- [ ] Serve static assets from FastAPI
- [ ] Configure production build integration
- [ ] Update routing for SPA deployment

#### 2. Enhanced MCP Server
- [ ] Add more chart types (scatter, pie, box plots, etc.)
- [ ] Implement data transformation tools
- [ ] Add chart customization options (colors, themes, annotations)
- [ ] Support for multiple data sources
- [ ] Chart export capabilities (PNG, SVG, PDF)

#### 3. Database Integration
- [ ] Add dummy database with sample datasets
- [ ] Implement data retrieval tools in MCP
- [ ] Create realistic sample data (sales, analytics, scientific)
- [ ] Add data filtering and aggregation tools

#### 4. RAG Integration (Potential)
- [ ] Implement RAG MCP server for data context
- [ ] Add document ingestion capabilities
- [ ] Enable natural language data queries
- [ ] Integrate with vector databases

#### 5. Production Features
- [ ] Authentication and authorization
- [ ] Rate limiting and request validation
- [ ] Error handling and logging improvements
- [ ] Performance optimization
- [ ] Docker containerization

## 🏃‍♂️ Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend Setup (Development)
```bash
cd frontend
npm install
npm run dev
```

### Environment Configuration
Create a `.env` file in the backend directory with your configuration:
```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_BASE_URL=thebase_url_for_your_LLM
LOG_LEVEL=INFO
```
Note that the existing MCP client expects message formats to follow that of Anthropic, currently works best with Claude Sonnet. Other LLM may not work due to inconsistent message formats between vendors.

## 🎮 Usage Example

Once running, you can interact with the chat API:

```bash
curl -X POST "http://localhost:8000/chat/query" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "content": "Create a line chart showing sales growth over 12 months, starting at $10k and growing 15% each month"
      }
    ]
  }'
```

The AI will process this request, use the MCP tools to generate a Plotly chart, and return the interactive visualization.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Technologies

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [FastMCP](https://github.com/jlowin/fastmcp)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Plotly](https://plotly.com/python/)
- [React](https://react.dev/)

---

*This project serves as a comprehensive example of building AI-powered data visualization systems using modern web technologies and the Model Context Protocol.*
