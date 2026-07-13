from sqlalchemy import Column, Integer, String, Date
from app.db.database import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)
    middle_names = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    birth_name = Column(String, nullable=True)
    preferred_name = Column(String, nullable=True)

    gender = Column(String, nullable=True)

    birth_date = Column(Date, nullable=True)
    birth_place = Column(String, nullable=True)

    death_date = Column(Date, nullable=True)
    death_place = Column(String, nullable=True)

    notes = Column(String, nullable=True)
    