from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from src.container import MCPContainer

from src.models.codel_request import CodeRequest
from tools.code_analysis_tool import CodeAnalysisTool
from tools.code_docstring_tool import CodeDocstringTool

router = APIRouter()

@router.post("/code-review", operation_id = "code-review",
             description="Bu endpoint gönderilen kodu analiz eder ve kod incelemesi yapar.")
@inject
async def code_review(
    request: CodeRequest,
    code_analysis_tool: CodeAnalysisTool = Depends(Provide[MCPContainer.code_analysis_tool])
):
    result = await code_analysis_tool(**request.parameters)
    return {"result": result}

@router.post("/code-docstring", operation_id = "code-docstring",
             description="Bu endpoint gönderilen kod parçacığı için docstring üretir." )
@inject
async def code_docstring(req: CodeRequest,
             code_docstring_tool : CodeDocstringTool = Depends(Provide[MCPContainer.code_docstring_tool])):
    result = await code_docstring_tool(**req.parameters)
    return {"result": result}
