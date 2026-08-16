from fastapi import HTTPException
from app.core.repo import create_session
import bcrypt
import hashlib
from app.core.security import create_access_tokens, create_refresh_tokens
class LoginService:
    def __init__(self, repo,db):
        self.repo = repo
        self.db = db

    def login(self,request,req):
        user = self.repo.get_user_by_email(request.email)
    
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        hashed_password=self.repo.get_hashed_password(user.user_id).artifact

        try:
            if not bcrypt.checkpw(request.password.encode('utf-8'), hashed_password):
                raise Exception("invalid password")
            access_token = create_access_tokens(data={"sub": str(user.user_id)})
            refresh_token = create_refresh_tokens(data={"sub": str(user.user_id)})
            hashed_refresh_token = hashlib.sha256(refresh_token.encode()).digest()
            create_session(
                user_id=user.user_id,
                db=self.db,
                hashed_refresh_token=hashed_refresh_token,
                ip_address=req.client.host,
                device_name=req.headers.get("User-Agent"),
            )
            self.db.commit()
            return {"access_token": access_token, "refresh_token": refresh_token}

        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=401, detail={"Invalid Password"})