from sqlalchemy_utils import create_database, database_exists

from p02_sqlalchemy.connect_db import db
from p02_sqlalchemy.models import Base

if not database_exists(db.url):
    create_database(db.url)  # creates database

Base.metadata.create_all(db)  # creates tables from classes in models.py
