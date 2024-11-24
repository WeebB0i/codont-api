from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_DE_DATOS: str 

    class Config:
        env_file = ".env"

settings = Settings()