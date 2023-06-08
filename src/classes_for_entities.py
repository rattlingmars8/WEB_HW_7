class StudentData:
    def __init__(self, id, fullname, group_id):
        self.id = id
        self.fullname = fullname
        self.group_id = group_id


class GroupData:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class TeacherData:
    def __init__(self, id, fullname):
        self.id = id
        self.fullname = fullname


class SubjectData:
    def __init__(self, id, sub_name, teacher_id):
        self.id = id
        self.sub_name = sub_name
        self.teacher_id = teacher_id


class GradeData:
    def __init__(self, id, subject_id, student_id, grade, date_of):
        self.id = id
        self.subject_id = subject_id
        self.student_id = student_id
        self.grade = grade
        self.time_of = date_of
