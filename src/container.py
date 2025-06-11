from dependency_injector import containers, providers

from tools.code_analysis_tool import CodeAnalysisTool
from tools.code_docstring_tool import CodeDocstringTool


class MCPContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["routers.agent"])
    code_analysis_tool = providers.Singleton(CodeAnalysisTool)
    code_docstring_tool = providers.Singleton(CodeDocstringTool)
