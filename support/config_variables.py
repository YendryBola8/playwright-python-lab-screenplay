import os
from typing import Optional

class Config:

    @staticmethod
    def get(key: str, default: Optional[str] = None) -> str:
        value = os.getenv(key, default)
        if value is None:
            raise ValueError(f"Variable de entorno '{key}' no encontrada y no se proporcionó valor por defecto")
        return value

    @staticmethod
    def get_base_url() -> str:
        return Config.get("BASE_URL", "")

    @staticmethod
    def get_username() -> str:
        return Config.get("USERNAME", "")

    @staticmethod
    def get_password() -> str:
        return Config.get("PASSWORD", "")

    @staticmethod
    def get_environment() -> str:
        return Config.get("ENVIRONMENT", "dev")