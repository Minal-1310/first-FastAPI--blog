from fastapi import APIRouter
from fastapi import APIRouter, Depends, status, HTTPException , status
from ..import database, models, database_models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user

router =  APIRouter(
    prefix= "/user",
    tags= ['Users']
)
get_db =  database.get_db

# create user
@router.post('', response_model=models.ShowUser,)
def create_user(request: models.User, db:Session = Depends(get_db)):
    return user.create(request, db)
 

@router.get('/{id}', response_model=models.ShowUser)
def get_user(id:int, db:Session = Depends(get_db)):
   return user.show(id, db)