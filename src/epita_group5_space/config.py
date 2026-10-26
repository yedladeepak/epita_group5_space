
import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")
    api_key: str = os.getenv("NASA_API_KEY", "")
    debug: bool = os.getenv("DEBUG", "False").lower() in (
        "true",
        "1",
        "yes",
    )

    def validate(self):
        """Check whether the NASA API key is configured."""
        if not self.api_key or self.api_key == "your_dummy_api_key_here":
            raise ValueError(
                "NASA API key is missing. "
                "Add NASA_API_KEY to your .env file."
            )


config = Settings()
