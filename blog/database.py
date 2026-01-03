from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

db_Url = "postgresql://postgres:Minal@localhost:5432/bitfumes"

engine = create_engine(db_Url)

SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind= engine)
Base = declarative_base()

def get_db():
    print("get db")
    db = SessionLocal()
    print("session")
    try:
        yield db 
    finally:
        db.close()