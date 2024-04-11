import os
from pathlib import Path

from pydantic_settings import BaseSettings
BASE_DIR = Path(__file__).parent.parent
class Settings(BaseSettings):
    db_url: str = f'sqlite+aiosqlite:///{BASE_DIR}/app.db'

settings = Settings()