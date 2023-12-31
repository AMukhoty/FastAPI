
from fastapi import APIRouter,Depends,status,HTTPException,Response

from typing import List
from sqlalchemy.orm import Session 
# from token import create_access_token
import token
import sys
sys.path.append('../')
import schemas,database,models,hashing
router=APIRouter(
  tags=['authentication']
)

@router.post('/login')
def login(request:schemas.Login,db: Session=Depends(database.getdb)):
  user=db.query(models.User).filter(models.User.email==request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid credentials')
  if not hashing.Hash.verify(user.password,request.password):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f'Invalid password')
  
   
    access_token =token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}