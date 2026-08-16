from app.core.services.ai_service.chatgpt import ChatGpt
from fastapi import HTTPException
class AgentService:
    def __init__(self, agent: ChatGpt,repo,db):
        self.agent = agent
        self.repo = repo
        self.db = db

    def create_agent(self,request,user_id):
        prompt = self.agent.get_prompt(request.model_dump())
        try:
            self.repo.create_agent(request,prompt,user_id)
            self.db.commit()
            return {"message": "Agent created successfully", "prompt": prompt}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error occurred while creating agent: {e}")

    def use_agent(self,req:str,agent_id:int,user):
        agent=self.repo.get_agent(agent_id)
        if agent is None:
            raise HTTPException(status_code=404, detail="Agent not found")
        if agent.user_id != user.user_id:
            raise HTTPException(status_code=403, detail="You are not authorized to use this agent")
        prompt = self.repo.get_prompt(agent_id)
        return self.agent.generate_response(req, prompt)

    def get_agents_bY_user(self,user_id:int):
        return self.repo.get_agents_by_user(user_id)