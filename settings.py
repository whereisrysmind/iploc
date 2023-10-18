from dotenv import load_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    ipstack_api_key: SecretStr
    ipstack_api_host: str

settings = Settings()
