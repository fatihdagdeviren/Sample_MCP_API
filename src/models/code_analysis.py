from pydantic import BaseModel


class CodeRequest(BaseModel):
    code: str


class AnalysisResponse(BaseModel):
    analysis: str