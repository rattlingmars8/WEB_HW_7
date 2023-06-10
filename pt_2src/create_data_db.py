from datetime import datetime
from uuid import uuid4
from sqlalchemy import desc

from pt_2src.pretty_output import pretty_output
from src.classes_for_entities import *
from src.db import session
from src.models import Subject, Teacher, Student, Group, Grade

@pretty_output(["ID", "Name"])
def create_group(name):
    group_id = session.query(Group).order_by(desc(Group.id)).first().id + 1
    group_name = name
    group = GroupData(group_id, group_name)
    group_obj = Group(group)
    session.add(group_obj)
    session.commit()
    return [group_id, group_name]


@pretty_output(["ID", "Name"])
def create_teacher(name):
    teacher_id = uuid4().hex[:6]
    teacher_name = name
    teacher = TeacherData(teacher_id, teacher_name)
    teacher_obj = Teacher(teacher)
    session.add(teacher_obj)
    session.commit()
    return [teacher_id, teacher_name]


@pretty_output(["ID", "Name", "GroupID"])
def create_student(name, gid):
    student_id = uuid4().hex[:6]
    student_name = name
    group_id = gid
    group = session.query(Group).filter_by(id=group_id).first()
    if not group:
        print(f"Group with ID={group_id} does not exist.")
        return
    student = StudentData(student_id, student_name, group_id)
    student_obj = Student(student)
    session.add(student_obj)
    session.commit()
    return [student_id, student_name, group_id]


@pretty_output(["ID", "Name", "TeacherID"])
def create_subject(subj_name, teacher_id):
    subject_id = session.query(Subject).order_by(desc(Subject.id)).first().id + 1
    subject_name = subj_name
    teacher_id = teacher_id
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if not teacher:
        print(f"Teacher with ID='{teacher_id}' does not exist.")
        return
    subject = SubjectData(subject_id, subject_name, teacher_id)
    subject_obj = Subject(subject)
    session.add(subject_obj)
    session.commit()
    return [subject_id, subject_name, teacher_id]


@pretty_output(["ID", "SubjectID", "StudentID", "Value", "Date"])
def create_grade(subject_id, student_id, grade_val):
    grade_id = session.query(Grade).order_by(desc(Grade.id)).first().id + 1
    date = datetime.today().date()
    subject = session.query(Subject).filter_by(id=subject_id).first()
    student = session.query(Student).filter_by(id=student_id).first()
    if not subject:
        print(f"Subject with ID={subject_id} does not exist.")
        return
    if not student:
        print(f"Student with ID={student_id} does not exist.")
        return
    grade = GradeData(grade_id, subject_id, student_id, grade_val, date)
    grade_obj = Grade(grade)
    session.add(grade_obj)
    session.commit()
    return [grade_id, subject_id, student_id, grade_val, date]
