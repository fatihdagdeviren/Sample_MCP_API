from http.client import HTTPException
import requests
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from models.mcp_request import MCPRequest
from src.container import MCPContainer

from src.models.tool_request import ToolRequest
from tools.code_analysis_tool import CodeAnalysisTool

router = APIRouter()

@router.post("/run-tool", operation_id = "run-tool")
@inject
async def run_tool(
    request: ToolRequest,
    code_analysis_tool: CodeAnalysisTool = Depends(Provide[MCPContainer.code_analysis_tool])
):

    # Tool'u çağır (__call__ üzerinden)
    result = await code_analysis_tool(**request.parameters)
    return {"result": result}

@router.get("/call-mcp", operation_id = "call-mcp")
def call_mcp(req: MCPRequest):
    return req
