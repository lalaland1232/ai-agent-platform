
import bcrypt
from fastapi import HTTPException

class SignUpService:
    def __init__(self,repo,db):
        self.repo = repo
        self.db = db

    def sign_up(self,request):
        user = self.repo.get_user_by_email_and_name(request.email,request.username)
        if user:
            raise HTTPException(status_code=400, detail="User already exists")
        try :
            user=self.repo.store_user(request)
            self.db.flush()
            salt=bcrypt.gensalt(rounds=12)
            hashed_password=bcrypt.hashpw(request.password.encode('utf-8'),salt)
            self.repo.store_artifact(user_id=user.user_id,hashed_password=hashed_password)
            self.db.commit()
            return {"message":"User created successfully"}
        except Exception as e:
            self.db.rollback()
            print(f"Error occurred during sign up: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")
        