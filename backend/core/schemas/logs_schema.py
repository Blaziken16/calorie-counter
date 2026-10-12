from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class LogBase(BaseModel):
    food_name: str = Field(min_length=3, max_length=50)
    calories: str = Field(min_length=2)
    logged_at: datetime

class LogCreate(LogBase):
    user_id : int

class LogUpdate(BaseModel):
    food_name: str | None = Field(default=None, min_length=3, max_length=50)
    calories: str | None = Field(default = None, min_length=2)
    
class LogResponse(LogBase):
    model_config = ConfigDict(from_attributes=True)
    id: int 
    user_id: int 


