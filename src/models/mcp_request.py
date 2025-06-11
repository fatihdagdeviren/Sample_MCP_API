# İstek gövdesi için model
from pydantic import BaseModel


class MCPRequest(BaseModel):
    tool: str
    input: str
