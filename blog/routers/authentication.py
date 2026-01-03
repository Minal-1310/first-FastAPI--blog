from fastapi import APIRouter
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, database, database_models, token
from ..hashing import Hash


router = APIRouter(tags= ['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm= Depends(), db: Session=Depends(database.get_db)):
    user = db.query(database_models.User).filter(database_models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    
    #generate a jwt token and return
    access_token =token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type": "bearer"}
    # return user