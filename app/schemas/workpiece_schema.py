from pydantic import BaseModel


class WorkpiecePydanticIn(BaseModel):
    name: str
    info: str | None = None
    status: str | None = None


class WorkpiecePydanticOut(BaseModel):
    id: int
    name: str
    info: str | None = None
    status: str | None = None
