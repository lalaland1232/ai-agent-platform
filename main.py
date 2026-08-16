from fastapi import FastAPI
from app.login.route import login_router
from app.signup.route import signup_router
from app.refresh.route import refresh_router
from app.agents.route import agent_router
app = FastAPI()
app.include_router(agent_router)
app.include_router(login_router)
app.include_router(signup_router)
app.include_router(refresh_router)
