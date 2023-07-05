from pydantic import BaseModel
from typing import List,Optional
#these are the pydantic models used for generating request body



#request models 
class Blog(BaseModel):
  title:str
  content:str
  user_id:int
  class Config():
    orm_mode=True
  

class Update(BaseModel):
  title:str 
  content:str
  
class User(BaseModel):
  username: str
  email:str
  password:str

#response bodies must have the config class in them 

class ShowUser(BaseModel):
  uname: str
  email:str
  blogs:List[Blog]=[]
  class Config():
    orm_mode=True
 

class ShowBlog(BaseModel):
  title:str
  content:str
  
  creator:ShowUser
  class Config():
    orm_mode=True

class Login(BaseModel):
  username:str
  password:str
 
  



  




  