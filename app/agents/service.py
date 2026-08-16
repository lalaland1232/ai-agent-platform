from app.core.services.ai_service.chatgpt import ChatGpt

class AgentService:
    def __init__(self, agent: ChatGpt,repo,db):
        self.agent = agent
        self.repo = repo
        self.db = db

    def create_agent(self,request):
        prompt = self.agent.get_prompt(request.dict())
        try:
            self.repo.create_agent(request,prompt)
            self.db.commit()
            return {"message": "Agent created successfully", "prompt": prompt}
        except Exception as e:
            return {"message": f"Error occurred while creating agent: {e}"}