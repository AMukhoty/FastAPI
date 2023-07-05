
#after CRUD OPS USING SQLALCGHEMY ORM IN FASTAPI

#changing the resposne body 
from fastapi import FastAPI
from database import engine
import models
from routers import blog,user,authentication



app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)






















