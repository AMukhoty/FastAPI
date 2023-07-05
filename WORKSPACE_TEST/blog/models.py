
#these are the sqlalchemy orm models used to generate the db schemas
from database import Base 
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
#sqlalchemy models used to generate the db schemas 

class Blog(Base):
  __tablename__ = "blogs_test"
  id=Column (Integer,primary_key = True,index=True)
  title=Column(String)
  content=Column(String)
  creator=relationship("User",back_populates="blogs")
  user_id=Column(Integer,ForeignKey('users.id'))

class User(Base):
  __tablename__ = "users"
  id=Column(Integer,primary_key = True,index=True)
  uname =Column (String)
  email=Column(String)
  password=Column(String)
  blogs=relationship("Blog",back_populates="creator")




