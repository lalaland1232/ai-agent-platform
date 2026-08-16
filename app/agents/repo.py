from app.db.models import Agent
from main import user_id
class AgentRepository:
    def __init__(self,db):
        self.db=db

    def create_agent(self,request,prompt):
        agent = Agent(
            user_id=user_id,
            work=request.agent_details,
            agent_prompt=prompt
        )
        self.db.add(agent)