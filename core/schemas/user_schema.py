from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UserBase(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    weight: str = Field(min_length = 4)
    height: str = Field(min_length = 4)

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    weight: str = Field(min_length = 4)
    height: str = Field(min_length = 4)

