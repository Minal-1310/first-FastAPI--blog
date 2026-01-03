from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException 
from ..import database_models, models

def get_all(db: Session):
    blog = db.query(database_models.Blog).all()
    return blog

def create(request: models.Blog, db: Session):
    new_blog = database_models.Blog(title=request.title, body=request.body,user_id=2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

def delete(id: int , db:Session):
    blog =db.query(database_models.Blog).filter(database_models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with id {id} not foind"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Delete Successfully!!'

def update(id: int, request:models.Blog,db: Session):
      blog = db.query(database_models.Blog).filter(database_models.Blog.id == id)
      if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
      
      blog.update(request.dict())
      db.commit()
      return 'Updated Successfully!!'


def show(id: int, db:Session):
    blog = db.query(database_models.Blog).filter(database_models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not availabe")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f"Blog with the id {id} is not availabe"}
    return blog

