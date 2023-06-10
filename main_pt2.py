from pt_2src.read_db import subjects_list, students_list, grades_list, groups_list, teachers_list
from pt_2src.create_data_db import create_group, create_grade, create_student, create_teacher, create_subject
from pt_2src.update_data_db import update_group, update_teacher, update_student, update_grade, update_subject
from pt_2src.delete_data_db import delete_group, delete_teacher, delete_student, delete_grade, delete_subject
from pt_2src.parser import parse_args


COMMANDS = {
    "create": {
        "Group": create_group,
        "Teacher": create_teacher,
        "Student": create_student,
        "Subject": create_subject,
        "Grade": create_grade,
    },
    "list": {
        "Group": groups_list,
        "Teacher": teachers_list,
        "Student": students_list,
        "Subject": subjects_list,
        "Grade": grades_list,
    },
    "update": {
        "Group": update_group,
        "Teacher": update_teacher,
        "Student": update_student,
        "Subject": update_subject,
        "Grade": update_grade,
    },
    "delete": {
        "Group": delete_group,
        "Teacher": delete_teacher,
        "Student": delete_student,
        "Subject": delete_subject,
        "Grade": delete_grade,
    },
}


def main():
    args = parse_args()
    action = args.action
    model = args.model
    name = args.name
    idf = args.identif

    if action == "list":
        if model == "Teacher":
            teachers_list()
        elif model == "Student":
            students_list()
        elif model == "Subject":
            subjects_list()
        elif model == "Grade":
            grades_list()
        elif model == "Group":
            groups_list()
        else:
            print("Invalid model")
    elif action == "create":
        if model == "Group":
            create_group(name)
        elif model == "Teacher":
            create_teacher(name)
        elif model == "Student":
            create_student(name, args.group_id)
        elif model == "Subject":
            create_subject(name, args.teacher_id)
        elif model == "Grade":
            create_grade(args.subject_id, args.student_id, args.grade)
        else:
            print("Invalid model")
    elif action == "update":
        if model == "Group":
            update_group(idf, name)
        elif model == "Teacher":
            update_teacher(idf, name)
        elif model == "Student":
            update_student(idf, name, args.group_id)
        elif model == "Subject":
            update_subject(idf, name, args.teacher_id)
        elif model == "Grade":
            update_grade(idf, args.grade)
        else:
            print("Invalid model")
    elif action == "delete":
        if model == "Group":
            delete_group(idf)
        elif model == "Teacher":
            delete_teacher(idf)
        elif model == "Student":
            delete_student(idf)
        elif model == "Subject":
            delete_subject(idf)
        elif model == "Grade":
            delete_grade(idf)
        else:
            print("Invalid model")
    else:
        print("Invalid action")


if __name__ == "__main__":
    main()
