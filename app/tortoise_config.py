"""
  app/tortoise_config.py
  Tortoise ORM Configuration
  This file is used to configure the Tortoise ORM for aerich
"""

from app.core.settings import settings

AERICH_CONFIG = settings.tortoise_orm_config_dict
