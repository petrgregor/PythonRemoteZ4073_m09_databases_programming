"""Exercise 2
● Add some grades for each student"""
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from models import *

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Grade(id=1, student=1, grade=2, date_created=datetime(2025, 1, 22, 12, 5)),
            Grade(student=5, grade=1, date_created=datetime(2025, 1, 22, 11, 5)),
            Grade(student=2, grade=3, date_created=datetime(2025, 1, 22, 10, 5)),
            Grade(student=8, grade=2, date_created=datetime(2025, 1, 22, 9, 5)),
            Grade(student=7, grade=4, date_created=datetime(2025, 1, 22, 8, 5)),
            Grade(student=5, grade=2, date_created=datetime(2025, 1, 21, 12, 5)),
            Grade(student=2, grade=1, date_created=datetime(2025, 1, 20, 10, 8)),
            Grade(student=1, grade=1, date_created=datetime(2025, 1, 22, 14, 50)),
            Grade(student=4, grade=2, date_created=datetime(2025, 1, 20, 12, 15)),
            Grade(student=8, grade=2, date_created=datetime(2025, 1, 18, 12, 18)),
            Grade(student=4, grade=1, date_created=datetime(2025, 1, 17, 12, 17)),
            Grade(student=4, grade=2, date_created=datetime(2025, 1, 15, 12, 25)),
            Grade(student=2, grade=3, date_created=datetime(2025, 1, 5, 12, 35)),
            Grade(student=1, grade=4, date_created=datetime(2025, 1, 12, 12, 45)),
            Grade(student=1, grade=3, date_created=datetime(2025, 1, 12, 12, 5)),
            Grade(student=2, grade=2, date_created=datetime(2025, 1, 22, 12, 5)),
            Grade(student=7, grade=1, date_created=datetime(2025, 1, 12, 12, 5)),
            Grade(student=5, grade=1, date_created=datetime(2025, 1, 13, 12, 5)),
            Grade(student=6, grade=1, date_created=datetime(2025, 1, 14, 12, 5)),
            Grade(student=5, grade=3, date_created=datetime(2025, 1, 15, 12, 5)),
            Grade(student=8, grade=2, date_created=datetime(2025, 1, 16, 12, 5)),
            Grade(student=4, grade=1, date_created=datetime(2025, 1, 17, 12, 5)),
            Grade(student=1, grade=2, date_created=datetime(2025, 1, 18, 12, 5)),
            Grade(student=1, grade=3, date_created=datetime(2025, 1, 19, 12, 5)),
            Grade(student=2, grade=2, date_created=datetime(2025, 1, 20, 12, 5))
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(e)
