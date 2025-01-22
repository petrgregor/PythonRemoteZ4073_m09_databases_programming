from sqlalchemy import text

from connect_db import db

# this dosn't work
#from models import Student, Base
#Base.metadata.create_all(db)

with db.connect() as conn:
    sql_statement = text("ALTER TABLE students ADD type_of_study VARCHAR(15);")
    conn.execute(sql_statement)
