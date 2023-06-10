from pt_2src.pretty_output import pretty_output
from src.db import session
from src.models import Subject, Teacher, Student, Group, Grade


@pretty_output(["ID", "Group name"])
def update_group(group_id, groupname):
    group = session.query(Group).filter_by(id=group_id).first()
    if not group:
        print(f"Group with ID={group_id} does not exist.")
    else:
        group.name = groupname
        session.commit()
        return [group_id, groupname]


@pretty_output(["ID", "Teacher name"])
def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if not teacher:
        print(f"Teacher with ID={teacher_id} does not exist.")
    else:
        teacher.name = name
        session.commit()
        return [teacher_id, name]


@pretty_output(["ID", "Student name", "Group ID"])
def update_student(student_id, student_name, group_id=None):
    student = session.query(Student).filter_by(id=student_id).first()
    gid = group_id
    if not student:
        print(f"Student with {student_id} does not exist.")
    else:
        student.fullname = student_name
        if gid is not None:
            student.group_id = gid
        session.commit()
        return [student_id, student_name, student.group_id]


@pretty_output(["ID", "Subject Name", "Teacher ID"])
def update_subject(subject_id, subject_name, teacher_id):
    subject = session.query(Subject).filter_by(id=subject_id).first()
    tid = teacher_id
    if not subject:
        print(f"Subject with ID={subject_id} does not exist.")
    else:
        subject.sub_name = subject_name
        if tid is not None:
            subject.teacher_id = tid
        session.commit()
        return [subject_id, subject.sub_name, subject.teacher_id]


@pretty_output(["Grade ID", "Student ID", "Subject ID", "Grade", "Date"])
def update_grade(grade_id, new_grade):
    grade = session.query(Grade).filter_by(id=grade_id).first()
    if not grade:
        print(f"Grade with ID {grade_id} does not exist.")
    else:
        grade.grade = new_grade
        session.commit()
        return [
            grade_id,
            grade.subject_id,
            grade.student_id,
            grade.grade,
            grade.time_of,
        ]