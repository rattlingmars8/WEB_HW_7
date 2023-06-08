import random

from datetime import datetime, date, timedelta
from uuid import uuid4
from faker import Faker

from src.classes_for_entities import *
from src.db import session
from src.models import Subject, Teacher, Student, Group, Grade

fake = Faker('uk-UA')

SUBJECTS = [
    "Математика",
    "Українська мова і література",
    "Історія України",
    "Фізика",
    "Хімія",
    "Біологія",
    "Економіка",
    "Комп'ютерні науки",
]

GROUP_NAMES = ["GGEYH-101",
               "PVZB-102",
               "MENND-103"
               ]


# Генерація випадкових даних і заповнення таблиць
def seed_student_data():
    data_of_students = []
    for _ in range(50):
        # Генерація унікального ідентифікатора студента
        student_id = uuid4().hex[:6]

        student_name = fake.name()
        group_id = fake.random_int(min=1, max=3)
        student = StudentData(student_id, student_name, group_id)
        data_of_students.append(student)

    return data_of_students


STUDENT_DATA = seed_student_data()


def seed_group_data() -> list[GroupData]:
    groups = []
    for id_, name in enumerate(GROUP_NAMES, 1):
        group = GroupData(id_, name)
        groups.append(group)
    return groups


GROUP_DATA = seed_group_data()


def seed_teacher_data() -> list[TeacherData]:
    teachers = []
    for _ in range(5):
        # Генерація унікального ідентифікатора вчителя
        teacher_id = uuid4().hex[:6]

        teacher_name = fake.name()
        teacher = TeacherData(teacher_id, teacher_name)
        teachers.append(teacher)
    return teachers


TEACHER_DATA = seed_teacher_data()


def seed_subject_data() -> list[SubjectData]:
    subject_data = []
    for id_, subject_name in enumerate(SUBJECTS, 1):
        # Вибір випадкового ідентифікатора вчителя зі списку вчителів
        teacher_id = random.choice([teacher.id for teacher in TEACHER_DATA])
        subject = SubjectData(id_, subject_name, teacher_id)
        subject_data.append(subject)
    return subject_data


SUBJECT_DATA = seed_subject_data()


def seed_grades_data():
    start_date = datetime.strptime("2023-01-16", "%Y-%m-%d")
    end_date = datetime.strptime("2023-11-25", "%Y-%m-%d")

    def get_list_dates(start: date, end: date):
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(days=1)
        return result

    list_dates = get_list_dates(start_date, end_date)

    list_of_Grades = []
    grade_id = 1

    for day in list_dates:
        subject_ids = [subject.id for subject in SUBJECT_DATA]
        rand_subject_ids = random.sample(subject_ids, random.randint(4, 5))
        rand_students = random.sample([student.id for student in STUDENT_DATA], random.randint(4, 5))

        for st in rand_students:
            for rand_subj in rand_subject_ids:
                grade = GradeData(grade_id, rand_subj, st, random.randint(1, 12), day.date())
                list_of_Grades.append(grade)
                grade_id += 1

    return list_of_Grades


GRADE_DATA = seed_grades_data()


def clear_tables():
    session.query(Grade).delete()
    session.commit()

    session.query(Subject).delete()
    session.commit()

    session.query(Student).delete()
    session.query(Group).delete()
    session.query(Teacher).delete()
    session.commit()


def seed_all():
    for group_data in GROUP_DATA:
        group = Group(group_data)
        session.add(group)
    session.commit()

    for student_data in STUDENT_DATA:
        student = Student(student_data)
        session.add(student)
    session.commit()

    for teacher_data in TEACHER_DATA:
        teacher = Teacher(teacher_data)
        session.add(teacher)
    session.commit()

    for subj_data in SUBJECT_DATA:
        subject = Subject(subj_data)
        session.add(subject)
    session.commit()

    for grade_data in GRADE_DATA:
        grade = Grade(grade_data)
        session.add(grade)
    session.commit()


if __name__ == "__main__":
    clear_tables()
    seed_all()




