from sqlalchemy.orm.exc import UnmappedInstanceError

from connect_db import session
from models import *

try:
    print("Change last name for student 'Helena Budíková' to 'Novotná':")
    student = session.query(Student).filter(Student.first_name == "Helena", Student.last_name == "Budíková").first()
    print(student)
    student.last_name = 'Novotná'
    session.commit()
    print(student)

except AttributeError as e:
    print(e)


try:
    print("Delete student 'Cyril Svoboda' from database:")
    student = session.query(Student).filter(Student.first_name == "Cyril", Student.last_name == "Svoboda").first()
    print(student)
    session.delete(student)
    session.commit()

except UnmappedInstanceError as e:
    print(e)
