from dependency_injector import containers, providers

from tools.code_analysis_tool import CodeAnalysisTool


class MCPContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["routers.agent"])
    code_analysis_tool = providers.Singleton(CodeAnalysisTool)
