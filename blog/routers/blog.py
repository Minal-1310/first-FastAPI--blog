from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import models, database, database_models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog


router =  APIRouter(
    prefix= "/blog",
    tags= ['Blogs']
)
get_db = database.get_db

@router.get('', response_model=List[models.showBlog])
def all(db: Session = Depends(get_db),current_user:models.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)
    




# Add api
@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: models.Blog, db: Session = Depends(get_db),current_user:models.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)
    


# delete by id api
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int,db: Session = Depends(get_db),current_user:models.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)


# update by id api 
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:models.Blog, db:Session= Depends(get_db),current_user:models.User = Depends(oauth2.get_current_user)):
  return blog.update(id,request, db)

@router.get('/{id}', status_code=200, response_model=models.showBlog)
def show(id: int, db: Session = Depends(get_db),current_user:models.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
   
