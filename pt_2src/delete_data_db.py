from src.db import session
from src.models import Subject, Teacher, Student, Group, Grade
from pt_2src.pretty_output import pretty_output


@pretty_output(["ID", "Group Name"])
def delete_group(group_id):
    group = session.query(Group).filter_by(id=group_id).first()
    group_name = group.name
    session.delete(group)
    session.commit()
    return [group_id, group_name]


@pretty_output(["ID", "Fullname", "Group ID"])
def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    student_name = student.fullname
    group_id = student.group_id
    session.delete(student)
    session.commit()
    return [student_id, student_name, group_id]


@pretty_output(["ID", "Fullname"])
def delete_teacher(teacher_id):
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    teacher_name = teacher.name
    session.delete(teacher)
    session.commit()
    return [teacher_id, teacher_name]


@pretty_output(["ID", "Name", "Teacher ID"])
def delete_subject(subject_id):
    subject = session.query(Subject).filter_by(id=subject_id).first()
    subject_name = subject.sub_name
    subject_teacher_id = subject.teacher_id
    session.delete(subject)
    session.commit()
    return [subject_id, subject_name, subject_teacher_id]


@pretty_output(["ID", "Subject ID", "Student ID", "Grade", "Date"])
def delete_grade(grade_id):
    grade = session.query(Grade).filter_by(id=grade_id).first()
    grade_value = grade.grade
    grade_subject_id = grade.subject_id
    grade_student_id = grade.student_id
    date = grade.time_of
    session.delete(grade)
    session.commit()
    return [grade_id, grade_subject_id, grade_student_id, grade_value, date]
