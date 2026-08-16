from fastapi import APIRouter, Depends, HTTPException
from app.refresh.service import RefreshService
from app.refresh.repo import RefreshRepository
from app.db.database import get_db
from app.core.security import get_token
refresh_router = APIRouter()
def get_repo(db=Depends(get_db)):
    return RefreshRepository(db)

def get_service(repo=Depends(get_repo), db=Depends(get_db)):
    return RefreshService(repo, db)

@refresh_router.post("/refresh")
def refresh_token(token = get_token(), service: RefreshService = Depends(get_service)):
    return service.refresh(token)