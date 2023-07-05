from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DB_URL='sqlite:///./blog.db'
# SQL_ALCHEMY_DB_URL='mysql://root:''@localhost/blog'

# Create an SQLite database engine
engine = create_engine(SQL_ALCHEMY_DB_URL,connect_args={"check_same_thread":False})

# # Create a session factory
SessionLocal = sessionmaker(bind=engine)


# Create a base class for declarative models
Base = declarative_base()

def getdb():
  db=SessionLocal()
  try:
    yield db
  finally:
    db.close()
