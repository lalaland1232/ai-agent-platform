from app.db.models import User,Artifact
import bcrypt
class SignUpRepository:
    def __init__(self,db):
        self.db = db

    def get_user_by_email_and_name(self,email,username):
        return self.db.query(User).filter(User.email == email, User.username == username).first()

    def store_user(self,request):
        user = User(
            username=request.username,
            email=request.email,
            
        )
        self.db.add(user)
        return user
    
    def store_artifact(self,user_id,hashed_password):
        
        artifact=Artifact(
            artifact_id=user_id,
            artifact=hashed_password
        )
        self.db.add(artifact)