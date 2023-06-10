from pprint import pprint

from sqlalchemy import func, desc
from sqlalchemy.sql.operators import and_

from src.db import session
from src.models import Student, Subject, Grade, Group, Teacher
from prettytable import PrettyTable


def select_1():
    """
    Знайти 5 студентів з найбільшим середнім балом по всім предметам.
    """
    query = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return query


def select_2(subject_name):
    """
    Знайти студента з найвищим середнім балом по певному предмету.
    """
    query = (
        session.query(Student.fullname, func.round(func.avg(Grade.grade)).label("average_grade"))
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Subject.id == Grade.subject_id)
        .filter(Subject.sub_name == subject_name)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(1)
    )
    result = query.first() if query.first() else None
    return result


def select_3(subject_name):
    """
    Знайти середній бал у групах з певного предмета.
    """
    query = (
        session.query(Group.name, func.round(func.avg(Grade.grade)).label("average_grade"))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Subject.id == Grade.subject_id)
        .filter(Subject.sub_name == subject_name)
        .group_by(Group.name)
        .all()
    )
    return query


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).
    """
    query = session.query(func.round(func.avg(Grade.grade)).label("average_grade"))
    result = query.scalar()
    return result


def select_5(teacher_name):
    """
    Знайти, які курси читає певний викладач.
    """
    query = (
        session.query(Subject.sub_name)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Teacher.name == teacher_name)
        .all()
    )
    return query


def select_6(group_name):
    """
    Знайти список студентів у певній групі.
    """
    query = (
        session.query(Student.fullname)
        .join(Group, Group.id == Student.group_id)
        .filter(Group.name == group_name)
        .all()
    )
    return query


def select_7(group_name, subject_name):
    """
    Знайти оцінки студентів в окремій групі з певного предмета.
    """
    query = (
        session.query(Group.name, Student.fullname, Subject.sub_name, Grade.grade)
        .join(Group, Group.id == Student.group_id)
        .join(Grade, Grade.student_id == Student.id)
        .join(Subject, Subject.id == Grade.subject_id)
        .filter(Group.name == group_name, Subject.sub_name == subject_name)
        .order_by(Group.name, Student.fullname)
        .all()
    )
    return query


def select_8(teacher_name):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    """
    query = (
        session.query(Teacher.name, Subject.sub_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
        .join(Subject, Subject.id == Grade.subject_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Teacher.name == teacher_name)
        .group_by(Teacher.name, Subject.sub_name)
        .all()
    )
    return query


def select_9(student_name):
    """
    Знайти список курсів, які відвідує певний студент.
    """
    query = (
        session.query(Student.fullname, Subject.sub_name)
        .join(Grade, Grade.subject_id == Subject.id)
        .join(Student, Student.id == Grade.student_id)
        .filter(Student.fullname == student_name)
        .group_by(Student.fullname, Subject.sub_name)
        .order_by(Subject.sub_name)
        .all()
    )
    return query


def select_10(student_name, teacher_name):
    """
    Знайти список курсів, які певному студенту читає певний викладач.
    """
    query = (
        session.query(Student.fullname, Subject.sub_name, Teacher.name)
        .join(Grade, Grade.student_id == Student.id)
        .join(Subject, Subject.id == Grade.subject_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Student.fullname == student_name, Teacher.name == teacher_name)
        .group_by(Student.fullname, Subject.sub_name, Teacher.name)
        .all()
    )
    return query
def select_11(teacher_name, student_name):
    """
    Знайти середній бал, який певний викладач ставить певному студентові.
    """
    query = (
        session.query(Teacher.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
        .join(Subject, Subject.id == Grade.subject_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .join(Student, Student.id == Grade.student_id)
        .filter(Teacher.name == teacher_name, Student.fullname == student_name)
        .group_by(Teacher.name, Student.fullname)
        .all()
    )
    return query


def select_12(group_name, subject_name):
    """
    Знайти оцінки студентів у певній групі з певного предмета на останньому занятті.
    """
    subquery = (
        session.query(Group.id, func.max(Grade.time_of).label('max_time_of'))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Group.name == group_name, Subject.sub_name == subject_name)
        .group_by(Group.id)
        .subquery()
    )

    query = (
        session.query(Group.name, Student.fullname, Subject.sub_name, Grade.grade, Grade.time_of)
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .join(subquery, and_(subquery.c.id == Group.id, subquery.c.max_time_of == Grade.time_of))
        .filter(Group.name == group_name, Subject.sub_name == subject_name)
        .order_by(Group.name, Student.fullname)
        .all()
    )
    return query

def save_results_to_file(results):
    """
    Зберігає результати у файл у вигляді таблиці.
    :param results: Словник, де ключі - назви результатів, значення - результати функцій
    """
    for result_name, result_data in results.items():
        table = PrettyTable()
        table.field_names = result_data["header"]
        table.add_rows(result_data["rows"])

        with open(f"{result_name}.txt", "w", encoding="utf-8") as file:
            file.write(f"{result_name}:\n")
            file.write(str(table))

        print(f"Result '{result_name}' saved to {result_name}.txt file.")



# pprint(select_12("GGEYH-101", "Математика"))

if __name__ == "__main__":
    # Виклики функцій та збереження результатів у словник
    results = {
        "Result 1": {
            "header": ["Fullname", "Average Grade"],
            "rows": select_1()
        },
        "Result 2": {
            "header": ["Fullname", "Average Grade"],
            "rows": [select_2('Математика')]
        },
        "Result 3": {
            "header": ["Group", "Average Grade"],
            "rows": select_3("Математика")
        },
        "Result 4": {
            "header": ["Average Grade"],
            "rows": [[select_4()]]
        },
        "Result 5": {
            "header": ["Subject"],
            "rows": select_5('Богдан Гречаник')
        },
        "Result 6": {
            "header": ["Fullname"],
            "rows": select_6('PVZB-102')
        },
        "Result 7": {
            "header": ["Group", "Fullname", "Subject", "Grade"],
            "rows": select_7('PVZB-102', "Біологія")
        },
        "Result 8": {
            "header": ["Teacher", "Subject", "Average Grade"],
            "rows": select_8("Богдан Гречаник")
        },
        "Result 9": {
            "header": ["Fullname", "Subject"],
            "rows": select_9("Тетяна Байда")
        },
        "Result 10": {
            "header": ["Fullname", "Subject", "Teacher"],
            "rows": select_10("Тетяна Байда", "Богдан Гречаник")
        },
        "Result 11": {
            "header": ["Teacher", "Student", "Average Grade"],
            "rows": select_11("Богдан Гречаник", "Лариса Атаманюк")
        },
        "Result 12": {
            "header": ["Group", "Fullname", "Subject", "Grade", "Date"],
            "rows": select_12("GGEYH-101", "Математика")
        }
    }

    save_results_to_file(results)
