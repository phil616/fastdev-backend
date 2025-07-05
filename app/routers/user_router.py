from fastapi import APIRouter

from app.core.loggers import logger
from app.schemas.user_schema import UserPydanticIn, UserPydanticOut
from app.service import user_service

user_router = APIRouter(prefix="/user")


@user_router.get("/all", response_model=list[UserPydanticOut])
async def get_all_users() -> list[UserPydanticOut]:
    return await user_service.get_all_users()


@user_router.post("/create", response_model=UserPydanticOut)
async def create_user(user_data: UserPydanticIn) -> UserPydanticOut:
    return await user_service.create_user(user_data)


@user_router.get("/{id}", response_model=UserPydanticOut)
async def get_user(id: int) -> UserPydanticOut:
    return await user_service.get_user(id)


@user_router.put("/{id}", response_model=UserPydanticOut)
async def update_user(id: int, user_data: UserPydanticIn) -> UserPydanticOut:
    logger.debug(f"Updating user with id {id}")
    return await user_service.update_user(id, user_data)


@user_router.delete("/{id}", status_code=204)
async def delete_user(id: int) -> None:
    return await user_service.delete_user(id)
