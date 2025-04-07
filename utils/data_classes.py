from pydantic import BaseModel, Field

class Light(BaseModel):
    """
    Represents the data structure of a light product.
    """
    title: str
    price: str
    reviews: int

class LLMConfigCustom(BaseModel):
    """
    Configuration for LLM access.
    """
    provider: str = Field(..., description="Name of the LLM provider")
    api_key: str = Field(..., description="API key for authentication")
