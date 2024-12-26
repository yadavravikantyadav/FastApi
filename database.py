from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL="mysql+pymysql://root:ravi@localhost/hitman"

engine = create_engine(DB_URL,echo=True)

SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()    