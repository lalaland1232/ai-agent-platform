import hashlib
from app.db.models import Session
import jwt 
from datetime import datetime,timezone
from fastapi import HTTPException
from app.core.config import settings
from app.core.security import create_access_tokens, create_refresh_tokens
class RefreshService:
    def __init__(self,repo,db):
        self.repo=repo
        self.db=db

    def refresh(self,token):
        payload = jwt.decode(jwt=token,key=settings.SERVER_SECRET,algorithms=["HS256"])
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")
        hashed_refresh_token = hashlib.sha256(token.encode()).digest()
        session = self.db.query(Session).filter(Session.hashed_refresh_token== hashed_refresh_token).first()
        if not session:
            raise Exception("Invalid refresh token")
        try:
            access_token = create_access_tokens(payload)
            refresh_token = create_refresh_tokens(payload)
            new_hashed_refresh_token = hashlib.sha256(refresh_token.encode()).digest()
            new_session = Session(
                user_id=session.user_id,
                hashed_refresh_token=new_hashed_refresh_token,
                ip_address=session.ip_address,
                device_name=session.device_name
            )
            self.db.add(new_session)
            session.revoked_at = datetime.now(timezone.utc)
            self.db.commit()
            return {"access_token": access_token, "refresh_token": refresh_token}
        except Exception as e:
            raise HTTPException(status_code=401, detail=f"hello brugg{e}")
        