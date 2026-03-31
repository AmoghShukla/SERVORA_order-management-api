from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL : str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    class config:
        env_file = ".env"

settings = Settings()