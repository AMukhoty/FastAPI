#users db 
from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session 
import sys
sys.path.append('../')
import schemas,database,models,hashing

router=APIRouter(
  tags=['users'],prefix='/user'
)
get_db=database.getdb

@router.post('/')
def create_user(request:schemas.User,db:Session= Depends(get_db)):
  
  new_user=models.User(uname=request.username,email=request.email,password=hashing.Hash.bcrypt(request.password))
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

# raise ValidationError(errors, field.type_)
# pydantic.error_wrappers.ValidationError: 1 validation error for ShowUser
# response since sql orm returns the value not as json so we have to use the config class in our orm 


@router.get('/{id}',response_model=schemas.ShowUser)#use of dco tags  with tags=['tagname]
def show_user(id,db:Session=Depends(get_db)):
  myuser=db.query(models.User).filter(models.User.id==id).first()
  if not myuser:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with user_id={id} not present')
  return myuser