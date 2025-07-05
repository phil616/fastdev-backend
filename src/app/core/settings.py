# app/core/settings.py

import json

from pydantic import Field, computed_field, model_validator
from pydantic_settings import BaseSettings
from typing_extensions import Self


class Settings(BaseSettings):

    env: str = Field("development", alias="ENV")

    # Application 配置, 自动挂载
    application_debug: str | None = None
    application_name: str | None = None
    application_version: str | None = None
    application_description: str | None = None

    @model_validator(mode="after")
    def _set_application_attributes(self) -> Self:
        with open(f".config/{self.env}.application.json", "r") as f:
            attributes = json.load(f)
        self.application_debug = attributes.get("app_debug")
        self.application_name = attributes.get("app_name")
        self.application_version = attributes.get("app_version")
        self.application_description = attributes.get("app_desc")
        return self

    @computed_field
    @property
    def tortoise_orm_config_dict(self) -> dict:  # type: ignore[type-arg]
        with open(f".config/{self.env}.database.json", "r") as f:
            return json.load(f)

    class Config:
        env_file = ".env"


# 默认设置
settings = Settings()
