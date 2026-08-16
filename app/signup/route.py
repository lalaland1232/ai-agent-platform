from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import SignUpRequest
from app.db.database import get_db
from app.signup.repo import SignUpRepository
from app.signup.service import SignUpService
signup_router=APIRouter()

def get_repo(db=Depends(get_db)):
    return SignUpRepository(db)

def get_service(repo=Depends(get_repo),db=Depends(get_db)):
    return SignUpService(repo=repo,db=db)

@signup_router.post("/signup")
def sign_up(request:SignUpRequest,service:SignUpService=Depends(get_service)):
    service.sign_up(request)