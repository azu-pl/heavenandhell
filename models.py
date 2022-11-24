from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_neme = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    pesel = Column(String(11), unique=True, nullable=False)
    phone = Column(String(20))
    adress = Column(String(50))

    courses = relationship(
        "Course",
        secondary="student_grades",
        back_populates="students"
    )


class OnlineCourse(Base):
    __tablename__ = 'online_courses'

    id = Column(Integer, ForeignKey("courses.course_id"), primary_key=True)
    url = Column(String(50), nullable=False)

    course = relationship("Course", back_populates="online_course")


class OnsiteCourse(Base):
    __tablename__ = 'onside_courses'

    id = Column(Integer, ForeignKey("courses.course_id"), primary_key=True)
    adress = Column(String(50), nullable=False)
    time = Column(String(10), nullable=False)
    days = Column(String(50))

    course = relationship("Course", back_populates="onsite_course")


class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    first_neme = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    pesel = Column(String(11), unique=True, nullable=False)
    phone = Column(String(20))
    adress = Column(String(50))
    enrollment_data = Column(DateTime, nullable=False, default=datetime.now)


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    budget = Column(Float, nullable=False)
    address = Column(String(50))


class Course(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    credits = Column
    department_id = Column(Integer, ForeignKey("departments.id"))
    start_date = Column(DateTime, default=datetime.now)
    end_date = Column(DateTime, default=datetime.now)
    price = Column(Float, nullable=False)

    department = relationship("Department", back_populates='courses')

    onsite_course = relationship("OnsiteCourse", back_populates="course")
    online_course = relationship("OnlineCourse", back_populates="course")

    students = relationship(
        "Student",
        secondary="student_grades",
        back_populates="courses"
    )


class StudentGrade(Base):
    __tablename__ = "student_grades"

    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    grade = Column(Float)


class Administrator(Base):
    __tablename__ = "administrators"

    stuff_id = Column(Integer, ForeignKey('stuff.id'))
    deperment_id = Column(Integer, ForeignKey('departments.id'))
    enrollment_date = Column(DateTime, ForeignKey('stuff.enrollment_data'))


class CourseInstructor(Base):
    __tablename__ = "course_instructors"

    course_id = Column(Integer, ForeignKey('courses.course_id'))
    stuff_id = Column(Integer, ForeignKey('stuff.id'))
    enrollment_date = Column(DateTime, ForeignKey('stuff.enrollment_data'))