from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from tortoise import Tortoise

from app.core.settings import settings


async def init_db() -> None:
    await Tortoise.init(
        config=settings.tortoise_orm_config_dict,
    )
    if settings.env == "test":
        await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await init_db()
    yield
    await close_db()
