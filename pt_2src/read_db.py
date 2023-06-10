from pt_2src.pretty_output import pretty_output
from src.db import session
from src.models import Subject, Teacher, Student, Group, Grade


#
# def pretty_output(columns):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 result = func(*args, **kwargs)
#                 entity_name = func.__name__.split("_")[1].capitalize()
#                 table = PrettyTable(columns)
#
#                 if "list" in func.__name__:
#                     if not result:
#                         print(f"{entity_name} table is empty")
#                     else:
#                         for item in result:
#                             table.add_row(item)
#                         print(table)
#                 elif "create" in func.__name__:
#                     if result:
#                         print(f"{entity_name} created successfully")
#                         table.add_row(result)
#                         print(table)
#                     else:
#                         print(f"No {entity_name} created")
#                 elif "update" in func.__name__:
#                     if result:
#                         print(f"{entity_name} update successfully.")
#                         table.add_row(result)
#                         print(table)
#                     else:
#                         print(f"No {entity_name} updated")
#                 elif "delete" in func.__name__:
#                     if result:
#                         print(f"{entity_name} was deleted successfully.")
#                         table.add_row(result)
#                         print(table)
#                     else:
#                         print("Error occurred.")
#                 else:
#                     print(f"Invalid function: {func.__name__}")
#             except AttributeError as e:
#                 print(f"Error: {e}")
#
#         return wrapper
#
#     return decorator
#

@pretty_output(["ID", "Name"])
def teachers_list(*args):
    teachers = session.query(Teacher).all()
    return [(teacher.id, teacher.name) for teacher in teachers]


@pretty_output(["ID", "Full Name", "Group ID"])
def students_list(*args):
    students = session.query(Student).all()
    return [(student.id, student.fullname, student.group_id) for student in students]


@pretty_output(["ID", "Subject Name"])
def subjects_list(*args):
    subjects = session.query(Subject).all()
    return [(subject.id, subject.sub_name) for subject in subjects]


@pretty_output(["ID", "Grade", "Student ID", "Subject ID", "Date"])
def grades_list(*args):
    grades = session.query(Grade).all()
    return [
        (grade.id, grade.grade, grade.student_id, grade.subject_id, grade.time_of)
        for grade in grades
    ]


@pretty_output(["ID", "Group name"])
def groups_list(*args):
    groups = session.query(Group).all()
    return [(group.id, group.name) for group in groups]
