from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./jobs.db"
    SCHEDULER_TIMEZONE: str = "UTC"

    class Config:
        env_file = ".env"

settings = Settings()
