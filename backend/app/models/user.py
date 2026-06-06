from ..database import Base
from sqlalchemy import Column,Integer,String,DateTime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password_hash = Column(String)
    created_at = Column(DateTime)