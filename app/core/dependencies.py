from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

class SignUpRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class CreateAgent(BaseModel):
    agent_name:str
    agent_details:str
    input_format:dict
    output_format:dict

class Use_Agent(BaseModel):
    req:dict
   