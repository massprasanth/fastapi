from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./app.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)


sessionlocal  = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
