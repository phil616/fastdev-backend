"""
  app/main.py
  FastAPI main file
  This file is used to start the application and provide uvicorn interfaces
  @author: phil616
  @date: 2025-06-12
  @license: GSSCL
"""

from fastapi import FastAPI

from app.core.lifespan import lifespan
from app.core.settings import settings
from app.routers.user_router import user_router
from app.routers.workpiece_router import workpiece_router

app = FastAPI(
    debug=settings.application_debug,
    title=settings.application_name,
    description=settings.application_description,
    version=settings.application_version,
    lifespan=lifespan,
)

app.include_router(user_router)
app.include_router(workpiece_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
