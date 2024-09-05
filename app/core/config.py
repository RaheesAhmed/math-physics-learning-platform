from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Math and Physics Educational Platform"
    PROJECT_VERSION: str = "1.0.0"
    ALLOWED_ORIGINS: list = ["http://localhost:3000"]  # Add your frontend URL here

    class Config:
        env_file = ".env"


settings = Settings()
