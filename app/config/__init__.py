from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_SETTINGS: str
