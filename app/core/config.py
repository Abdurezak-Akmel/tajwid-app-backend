# Database Settings

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Pydantic automatically looks for matching env variables (case-insensitive)
    # Fall-back values
    db_host: str = "localhost" 
    db_port: int = 3306
    db_user: str = "root"
    db_password: str
    db_name: str = "tejwid"

    # Security Settings
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    api_base_url: str = "http://localhost:8000"

    # Mail Settings
    mail_username: str = ""
    mail_password: str = ""
    mail_from: str = ""
    mail_port: int = 587
    mail_server: str = "smtp.gmail.com"
    mail_from_name: str = "Tejwid App"

    # Alternatively, you can build the full connection string dynamically
    @property
    def database_url(self) -> str:
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    # Configuration for Pydantic Settings
    model_config = SettingsConfigDict(
        env_file=".env",            # Tells Pydantic to read from a .env file
        env_file_encoding="utf-8",
        extra="ignore"              # Ignores other random env variables in your system
    )

# Instantiate the settings object so it can be imported elsewhere
settings = Settings()