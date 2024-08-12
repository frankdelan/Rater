from dotenv import load_dotenv

from pydantic_settings import SettingsConfigDict, BaseSettings

load_dotenv()


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DATABASE: str

    @property
    def DB_URL(self) -> str:
        return (f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
                f"{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}")

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
