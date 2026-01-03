from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .database import Base  

# Base = declarative_base()/
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, index= True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")

class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key= True, index= True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")



  