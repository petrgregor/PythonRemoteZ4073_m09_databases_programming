from connect_db import session
from models import *

print("Join student with their lockers, print students owning locker:")
results = session.query(Student).join(Locker)
print(results)
for result in results:
    print(result)

print('-'*80)
print("Join student with their lockers, print students with their locker:")
results = session.query(Student, Locker).join(Locker)
print(results)
for result in results:
    print(result)
print('-'*40)
for result in results:
    student, locker = result
    print(f"{locker}, {student}")

print('-'*80)
print("Join student with their lockers, print students with their locker sorted by locker number:")
results = session.query(Student, Locker).join(Locker).order_by(Locker.number)
for result in results:
    student, locker = result
    print(f"{locker}, {student}")

print('-'*80)
print("Join student with their lockers, print students with number of their locker sorted by locker number:")
results = session.query(Student, Locker.number).join(Locker).order_by(Locker.number)
for result in results:
    student, locker = result
    print(f"#{locker}: {student}")

print('-'*80)
print("Student with locker #4:")
results = session.query(Student).join(Locker).filter(Locker.number == 4)
for result in results:
    print(result)
