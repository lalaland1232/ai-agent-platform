user_id=1
from fastapi import FastAPI
app = FastAPI()
from app.agents.route import agent_router
app.include_router(agent_router)
