from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_DE_DATOS: str 
    API_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings()