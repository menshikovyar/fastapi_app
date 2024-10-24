from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pydantic import PostgresDsn #строчка подключения к базе

class ApiPrefix(BaseModel):
  prefix: str = "/api"

class DataBaseConfig(BaseModel):
  db: PostgresDsn

class Settings(BaseSettings):
  api: ApiPrefix = ApiPrefix()
  db: DataBaseConfig

settings = Settings()
