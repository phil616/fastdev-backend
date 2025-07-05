from pydantic import BaseModel


class UserPydanticIn(BaseModel):
    username: str
    password: str


class UserPydanticOut(BaseModel):
    id: int
    username: str
