from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class LogBase(BaseModel):
    foodName: str = Field(min_length=3, max_length=50)
    calories: str = Field(min_length=2)
    

class LogCreate(LogBase):
    user_id : int
    loggedAt: datetime

class LogUpdate(BaseModel):
    foodName: str | None = Field(min_length=3, max_length=50)
    calories: str | None = Field(min_length=2)
    
class LogResponse(LogBase):
    model_config = ConfigDict(from_attributes=True)
    id: int 
    user_id: int 
    loggedAt: datetime


