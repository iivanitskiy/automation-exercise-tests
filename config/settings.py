from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    base_url: str = "https://automationexercise.com"
    api_base_url: str = "https://automationexercise.com/api"
    headless: bool = True
    slow_mo: int = 0
    default_timeout: int = 30_000

    @property
    def timeout_ms(self) -> int:
        return self.default_timeout


@lru_cache
def get_settings() -> Settings:
    return Settings()
