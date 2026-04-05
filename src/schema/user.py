from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    user_name: str = Field(..., min_length=2, max_length=50)
    user_phone: str = Field(..., min_length=10, max_length=15)
    user_email: EmailStr