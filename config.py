from pathlib import Path
from pydantic import BaseSettings
from typing import Any


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    return_limit: int = 100

    class Config:
        env_file = Path(__file__).resolve().parent / ".env"


class Paths(BaseSettings):
    base_path: Path = Path(__file__).resolve().parent
    data_path: Path = base_path / "data"

    def __init__(self, **values: Any):
        super().__init__(**values)

        self.data_path.mkdir(exist_ok=True)


settings = Settings()
paths = Paths()
