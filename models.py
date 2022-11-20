from sqlalchemy import Column, Integer, String
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