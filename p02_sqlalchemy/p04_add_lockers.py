from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from models import *

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Locker(number=1, student=5),
            Locker(number=2, student=6),
            Locker(number=3, student=8),
            Locker(number=4, student=2),
            Locker(number=5, student=7),
            Locker(number=6, student=4),
            Locker(number=7, student=1),
            Locker(number=8, student=2)
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(e)
