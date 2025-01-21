import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database>
#db = create_engine(f"mysql+mysqlconnector://test:test@localhost:3306/school")
# není vhodné vkládat do zdrojového kódu reálná hesla a další citlivé údaje

# můžeme použít proměnné ze souboru, který není součástí repozitáře
#from p01_mysql.connection_details import *
#db = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:3306/school")

# nebo můžeme využít dotenv prostředí
load_dotenv()
db = create_engine(f"mysql+mysqlconnector://{os.getenv('user', default='test')}:"
                   f"{os.getenv('password', default='test')}@"
                   f"{os.getenv('host', default='localhost')}:"
                   f"{os.getenv('port', default=3306)}"
                   f"/school")

Session = sessionmaker(bind=db)
session = Session()

print(f"db.url = {db.url}")
