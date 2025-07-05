from fastapi import APIRouter

from app.schemas.workpiece_schema import WorkpiecePydanticIn, WorkpiecePydanticOut
from app.service.workpiece_service import (
    create_workpiece,
    delete_workpiece,
    get_workpiece,
    update_workpiece,
)

workpiece_router = APIRouter(prefix="/workpiece")


@workpiece_router.get("/{id}", response_model=WorkpiecePydanticOut)
async def router_get_workpiece(id: int) -> WorkpiecePydanticOut | None:
    return await get_workpiece(id)


@workpiece_router.post("", response_model=WorkpiecePydanticOut)
async def router_create_workpiece(
    workpiece_in: WorkpiecePydanticIn,
) -> WorkpiecePydanticOut:
    return await create_workpiece(workpiece_in)


@workpiece_router.put("/{id}", response_model=WorkpiecePydanticOut)
async def router_update_workpiece(
    id: int, workpiece_in: WorkpiecePydanticIn
) -> WorkpiecePydanticOut | None:
    return await update_workpiece(id, workpiece_in)


@workpiece_router.delete("/{id}", response_model=None)
async def router_delete_workpiece(id: int) -> None:
    return await delete_workpiece(id)
