from dotenv import load_dotenv
load_dotenv()
import os
from dataclasses import dataclass
@dataclass
class Config:
    DATABASE_URL:str = os.getenv("DATABASE_URL")
    SERVER_SECRET:str = os.getenv("SERVER_SECRET")
    ACCESS_TOKEN_EXPIRE_MINUTES:int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    REFRESH_TOKEN_EXPIRE_DAYS:int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))

settings = Config()