from app.db.models import Agent

class AgentRepository:
    def __init__(self,db):
        self.db=db

    def create_agent(self,request,prompt,user_id):
        agent = Agent(
            agent_name=request.agent_name,
            user_id=user_id,
            work=request.agent_details,
            agent_prompt=prompt
        )
        self.db.add(agent)

    def get_prompt(self,agent_id:int):
        prompt=self.db.query(Agent.agent_prompt).filter(Agent.agent_id==agent_id).first()
        return prompt
    def get_agent(self,agent_id:int):
        agent=self.db.query(Agent).filter(Agent.agent_id==agent_id).first()
        return agent
    def get_agents_by_user(self,user_id:int):
        agents=self.db.query(Agent).filter(Agent.user_id==user_id).all()
        return agents