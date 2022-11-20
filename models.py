from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_neme = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    pesel = Column(String(11), unique=True, nullable=False)
    phone = Column(String(20))
    adress = Column(String(50))


class OnlineCourse(Base):
    __tablename__ = 'online_courses'

    id = Column(Integer, primary_key=True)
    url = Column(String(50), nullable=False)


class OnsiteCourse(Base):
    __tablename__ = 'onside_courses'

    id = Column(Integer, primary_key=True)
    adress = Column(String(50), nullable=False)
    time = Column(String(10), nullable=False)
    days = Column(String(50))


class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    first_neme = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    pesel = Column(String(11), unique=True, nullable=False)
    phone = Column(String(20))
    adress = Column(String(50))
    enrollment_data = Column(DateTime, nullable=False, default=datetime.now)
