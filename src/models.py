from sqlalchemy import Column, Integer, String, ForeignKey, Date, func
from sqlalchemy.orm import relationship, declarative_base

from src.classes_for_entities import StudentData, GroupData, TeacherData, GradeData, SubjectData

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(String, primary_key=True)
    fullname = Column(String)
    group_id = Column(Integer, ForeignKey("groups.id"))

    group = relationship("Group", backref="students")

    def __init__(self, student_data: StudentData):
        self.id = student_data.id
        self.fullname = student_data.fullname
        self.group_id = student_data.group_id


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, group_data: GroupData):
        self.id = group_data.id
        self.name = group_data.name


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(String, primary_key=True)
    name = Column(String)

    subjects = relationship("Subject", backref="teacher")

    def __init__(self, teacher_data: TeacherData):
        self.id = teacher_data.id
        self.name = teacher_data.fullname


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    sub_name = Column(String)
    teacher_id = Column(String, ForeignKey("teachers.id"))

    def __init__(self, subject_data: SubjectData):
        self.id = subject_data.id
        self.sub_name = subject_data.sub_name
        self.teacher_id = subject_data.teacher_id


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    student_id = Column(String, ForeignKey("students.id"))
    grade = Column(Integer)
    time_of = Column(Date)

    subject = relationship("Subject", backref="grades")
    student = relationship("Student", backref="grades")

    def __init__(self, grade_data: GradeData):
        self.id = grade_data.id
        self.subject_id = grade_data.subject_id
        self.student_id = grade_data.student_id
        self.grade = grade_data.grade
        self.time_of = grade_data.time_of
