from pydantic_settings import BaseSettings
from pydantic import BaseModel

class ApiPrefix(BaseModel):
  prefix: str = "/api"

class Settings(BaseSettings):
  api: ApiPrefix = ApiPrefix()

settings = Settings()
