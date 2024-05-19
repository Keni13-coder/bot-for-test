from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str = Field(default='mongodb://localhost:27017')
    mongo_db: str = Field(default='company')
    bot_token: str = Field(default='YOUR_BOT_TOKEN')
    rate_limit_message: int = Field(default=1, description='Нужен для определение кол-во разрешенный сообщений')
    
    class Config:
        env_file = ".env"

settings = Settings()
