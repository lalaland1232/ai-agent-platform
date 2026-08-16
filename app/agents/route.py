from fastapi import APIRouter, Depends
from app.agents.service import AgentService
from app.db.database import get_db
from app.agents.repo import AgentRepository
from app.core.dependencies import CreateAgent
from app.core.services.ai_service.chatgpt import ChatGpt
agent_router=APIRouter()
def get_agent():
    return ChatGpt()

def get_repo(db=Depends(get_db)):
    return AgentRepository(db)

def get_service(agent=Depends(get_agent),repo=Depends(get_repo),db=Depends(get_db)):
    return AgentService(agent,repo,db)


@agent_router.post("/create_agent")
def create_agent(request:CreateAgent,service=Depends(get_service)):
    return service.create_agent(request)
    