from app.core.loggers import logger
from app.models.user import User
from app.schemas.user_schema import UserPydanticIn

# User CURD


async def create_user(user_data: UserPydanticIn) -> User:
    """
    User Create aka register
    """
    return await User.create(**user_data.model_dump())


async def get_all_users() -> list[User]:
    return await User.all()


async def delete_user(user_id: int) -> None:
    await User.filter(id=user_id).delete()


async def update_user(user_id: int, user_data: UserPydanticIn) -> User:
    logger.debug(f"Updating user with id {user_id}")
    current_user = await User.filter(id=user_id).first()
    logger.debug(current_user.__dict__)
    logger.debug(user_data.model_dump())
    current_user.update_from_dict(user_data.model_dump())
    await current_user.save()
    logger.info(f"{current_user}")
    return current_user


async def get_user(user_id: int) -> User:
    return await User.get(id=user_id)
