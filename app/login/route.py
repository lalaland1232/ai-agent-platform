from fastapi import APIRouter, Depends,Request
from app.core.dependencies import LoginRequest
from app.login.service import LoginService
from app.db.database import get_db
from app.login.repo import LoginRepository

login_router = APIRouter()

def get_repo(db=Depends(get_db)):
    return LoginRepository(db)

def get_service(repo=Depends(get_repo), db=Depends(get_db)):
    return LoginService(repo, db)

@login_router.post("/login")
def login(request:LoginRequest,req:Request, service=Depends(get_service)):
    return service.login(request,req)