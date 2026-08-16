

import jwt
from datetime import datetime, timedelta , timezone
from app.core.config import settings
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.db.database import get_db
from app.db.models import User
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
def get_token(token=Depends(oauth2_scheme)):
    return token


def create_token(payload):
    token = jwt.encode(payload,settings.SERVER_SECRET,algorithm="HS256")
    return token

def create_access_tokens(data):
    payload=data.copy()
    payload["type"]="access"
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload["exp"]=expire
    return create_token(payload)

def create_refresh_tokens(data):
    payload=data.copy()
    payload["type"]="refresh"
    expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    payload["exp"]=expire
    return create_token(payload)

def get_current_user(db=Depends(get_db),token=Depends(get_token)):
    payload=jwt.decode(token,settings.SERVER_SECRET,algorithms=["HS256"])
    if payload["type"]!="access":
        raise Exception("Invalid token type")
    user_id = payload["sub"]

    user = db.get(User,int(user_id))
    return user
    
   
    
