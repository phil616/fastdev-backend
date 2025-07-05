from fastapi import HTTPException

from app.core.loggers import logger
from app.models.workpiece import Workpiece
from app.schemas.workpiece_schema import WorkpiecePydanticIn, WorkpiecePydanticOut

# workpiece curd


async def create_workpiece(workpiece_in: WorkpiecePydanticIn) -> WorkpiecePydanticOut:
    return await Workpiece.create(**workpiece_in.model_dump())


async def get_workpiece(id: int) -> Workpiece | None:
    return await Workpiece.get_or_none(id=id)


async def delete_workpiece(id: int) -> None:
    workpiece = await Workpiece.get_or_none(id=id)
    if workpiece:
        await workpiece.delete()
        return None
    raise HTTPException(status_code=404, detail="Workpiece not found")


async def update_workpiece(
    id: int, workpiece_in: WorkpiecePydanticIn
) -> Workpiece | None:
    workpiece = await get_workpiece(id)
    if workpiece:
        logger.debug(f"Updating workpiece with id {id},({workpiece_in.model_dump()}")
        workpiece.update_from_dict(workpiece_in.model_dump())
        await workpiece.save()
        return workpiece
    else:
        raise HTTPException(status_code=404, detail="Workpiece not found")
