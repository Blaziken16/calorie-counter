from pydantic import BaseModel, ConfigDict, Field

class UserBase(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    weight: str = Field(min_length = 4)
    height: str = Field(min_length = 4)

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str |None = Field(default = None, min_length=3, max_length=20)
    weight: str|None = Field(default = None, min_length = 4)
    height: str|None = Field(default = None, min_length = 4)

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


