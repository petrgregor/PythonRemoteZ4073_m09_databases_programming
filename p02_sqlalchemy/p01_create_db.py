from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from p02_sqlalchemy.models import Base
from p01_mysql.connection_details import *

# mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database>
#db = create_engine(f"mysql+mysqlconnector://test:test@localhost:3306/school")
db = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:3306/school")

Session = sessionmaker(bind=db)
session = Session()

print(f"db.url = {db.url}")

if not database_exists(db.url):
    create_database(db.url)

Base.metadata.create_all(db)
