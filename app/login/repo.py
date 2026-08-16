
from app.db.models import Artifact, User


class LoginRepository:
    def __init__(self, db):
        self.db = db

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_hashed_password(self, user_id: int):
        return  self.db.query(Artifact).filter(Artifact.artifact_id == user_id).first()
        