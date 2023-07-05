from fastapi import APIRouter,Depends,status,HTTPException,Response

from typing import List
from sqlalchemy.orm import Session 
import sys
sys.path.append('../')
import schemas,database,models

router=APIRouter(
  tags=['blogs'],
  prefix='/blog'
)
get_db=database.getdb

#to get all records of db 


#This error occurs because we have to use List 
#pydantic.error_wrappers.
# ValidationError: 2 validation errors for ShowBlog
# response -> title
#   field required (type=value_error.missing)
# response -> content field required (type=value_error.missing)

@router.get('/',tags=['blogs'],response_model=List[schemas.ShowBlog])
def all(db: Session=Depends(get_db)):
  blogs=db.query(models.Blog).all()
  return blogs


#to create a new blog 
@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db: Session=Depends(get_db)):
  new_blog=models.Blog(title=request.title,content=request.content,user_id=request.user_id)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

# to get records of db with id provided in the dynamic routing as the path url and providing custom status code using status of fastAPI 
#as well as HTTPException class as well 
@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,db: Session=Depends(get_db)):
  blog=db.query(models.Blog).filter(models.Blog.id==id).first()
  if not blog:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id={id} not available')
    # response.status_code=status.HTTP_404_NOT_FOUND
    # return {'detail':f'Blog with id={id} not available'}
  return blog



#to delete a row

@router.delete("/{id}")
def delete(id,db: Session=Depends(get_db)):
  blog=db.query(models.Blog).filter(models.Blog.id==id)
  if not blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id={id} not present')
  blog.delete(synchronize_session=False)
  db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)




#to update a row 
#remember request is not a dict type so it doesn't directly 
# pass the values we pass in the request body so we need to typecast it to dict type object 

@router.put("/{id}")
def update(id,request:schemas.Update,db: Session=Depends(get_db)):
  blog=db.query(models.Blog).filter(models.Blog.id==id)
  if not blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id={id} not present')
  
  blog.update(request.dict())
  # blog.update('title':request.title,'content':request.content)
  db.commit()
  return Response(status_code=status.HTTP_202_ACCEPTED)

