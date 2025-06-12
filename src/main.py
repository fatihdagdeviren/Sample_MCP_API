from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from routers import agent
from src.container import MCPContainer
from fastapi_mcp import FastApiMCP

@asynccontextmanager
async  def lifespan(app : FastAPI):
    print("Starting")
    container = MCPContainer()
    # # Dependency Injector
    app.container = container
    # Register routers
    app.include_router(agent.router, tags=["MCP Tools"])
    mcp = FastApiMCP(app,
                     name="API MCP",
                     description="MCP server for the Item API",
                     describe_full_response_schema=True,  # Describe the full response JSON-schema instead of just a response example
                     describe_all_responses=True,  # Describe all the possible responses instead of just the success (2XX) response
                     )
    # Mount the MCP server directly to your FastAPI app
    # https://app.base.url/mcp
    mcp.mount()
    yield

    print("End")

app = FastAPI(
        title="MCP Agent API",
        description="Modular Tool Agent Server using FastMCP",
        version="1.0.0",
        lifespan=lifespan
    )
#
# # # Define your endpoints as you normally would
# @app.get("/items2",operation_id= "get_item2")
# async def read_item(item_id: int):
#     return {"item_id": item_id, "name": f"Item {item_id}"}



if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=False)

