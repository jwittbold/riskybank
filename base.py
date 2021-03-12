
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from toml_config import db_url


# creates the engine and unpacks all the values from 'db_url' variable located in toml_config.py module
try:
    engine = create_engine(URL(**db_url))

except SQLAlchemyError as e:
    error = str(e.__dict__['orig'])
    print(type(e))

# creates a session and binds it to the engine
Session = sessionmaker(bind=engine)
session = Session()

# # declares the base class for relationships between classes
Base = declarative_base()


