from app.db.database import Base
from sqlalchemy import DateTime, Integer, LargeBinary,String,ForeignKey, UniqueConstraint,func
from sqlalchemy.orm import relationship, Mapped,mapped_column
from datetime import datetime,timezone

class User(Base):
    __tablename__="users"
    user_id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    username:Mapped[str]=mapped_column(String(255),nullable=False,unique=True)
    email:Mapped[str]=mapped_column(String(255),nullable=False,unique=True)

    
    artifact:Mapped["Artifact"]=relationship("Artifact",back_populates="user",cascade="all, delete-orphan")

    agents:Mapped[list["Agent"]]=relationship("Agent",back_populates="user",cascade="all, delete-orphan")
class Artifact(Base):
    __tablename__="artifacts"
    artifact_id:Mapped[int]=mapped_column(Integer,ForeignKey("users.user_id"),primary_key=True,index=True)
    artifact:Mapped[bytes]=mapped_column(LargeBinary,nullable=False)    

    user:Mapped["User"]=relationship("User",back_populates="artifact")

class Session(Base):
    __tablename__="sessions"
    session_id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    user_id:Mapped[int]=mapped_column(Integer,ForeignKey("users.user_id"),nullable=False)
    hashed_refresh_token:Mapped[bytes]=mapped_column(LargeBinary,nullable=False)
    created_at:Mapped[datetime] = mapped_column(DateTime,nullable=False,server_default=func.now())
    revoked_at:Mapped[datetime | None]=mapped_column(DateTime,nullable=True)
    ip_address:Mapped[str]=mapped_column(String(45),nullable=False)
    device_name:Mapped[str]=mapped_column(String(255),nullable=False)

class Agent(Base):
    __tablename__="agents"
    __table_args__=(UniqueConstraint("user_id","agent_name",name="uq_user_agent_name"),)
    agent_id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    user_id:Mapped[int]=mapped_column(Integer,ForeignKey("users.user_id"),nullable=False)
    agent_name:Mapped[str]=mapped_column(String(255),nullable=False)
    work:Mapped[str]=mapped_column(String(255),nullable=False)
    agent_prompt:Mapped[str]=mapped_column(String,nullable=False)   

    user:Mapped["User"]=relationship("User",back_populates="agents")