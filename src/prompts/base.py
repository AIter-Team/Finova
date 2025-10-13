from typing_extensions import Optional
from pydantic import BaseModel, Field

class PromptConfig(BaseModel):
    model: str = Field(default="gemini-2.5-flash")
    temperature: Optional[float] = Field(default=0.5)
    orchestrator: Optional[str] = Field(default=None)

class Prompt(BaseModel):
    name: str = Field(description="Prompt name or title")
    prompt: str = Field(description="Prompt string", default="You are a helpful assistant")
    type: str = Field(description="Prompt Type (text or chat)", default="text")
    config: PromptConfig

