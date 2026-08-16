from fastapi import APIRouter, Depends
from app.agents.service import AgentService
from app.db.database import get_db
from app.agents.repo import AgentRepository
from app.core.dependencies import CreateAgent,Use_Agent
from app.core.services.ai_service.chatgpt import ChatGpt
from app.core.security import get_current_user
agent_router=APIRouter()
def get_agent():
    return ChatGpt()

def get_repo(db=Depends(get_db)):
    return AgentRepository(db)

def get_service(agent=Depends(get_agent),repo=Depends(get_repo),db=Depends(get_db)):
    return AgentService(agent,repo,db)


@agent_router.post("/create_agent")
def create_agent(request:CreateAgent,service=Depends(get_service),current_user=Depends(get_current_user)):
    return service.create_agent(request,current_user.user_id)

@agent_router.post("/agent/{agent_id}")
def use_agent(req:Use_Agent,agent_id:int,service=Depends(get_service),current_user=Depends(get_current_user)):
    return service.use_agent(req.req, agent_id,current_user)

@agent_router.get("/agents_by_user")
def get_agents_by_user(service=Depends(get_service),current_user=Depends(get_current_user)):
    
    return service.get_agents_bY_user(current_user.user_id)