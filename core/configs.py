from pydantic import BaseConfig
from fastapi.templating import Jinja2Templates
from pathlib import Path
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseConfig):
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/startup"
    DBBaseModel = declarative_base()
    TEMPLATES = Jinja2Templates(directory="templates")
    MDEIA = Path("media")

    class Config:
        case_sensitive = True


settings: Settings = Settings()
