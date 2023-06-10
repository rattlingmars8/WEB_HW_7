import argparse


def parse_args():
    PARSE_COMMANDS = {
        "create": {
            "Grade": {"-g": "--grade", "-sid": "--subject_id", "-stid": "--student_id"},
            "Student": {"-gid": "--group_id"},
            "Subject": {"-tid": "--teacher_id"},
            "Group": {},
            "Teacher": {}
        },
        "update": {
            "Group": {},
            "Teacher": {},
            "Student": {"-gid": "--group_id"},
            "Subject": {"-tid": "--teacher_id"},
            "Grade": {"-g": "--grade"},
        },
        "list": {"Group": {}, "Teacher": {}, "Student": {}, "Subject": {}, "Grade": {}},
        "delete": {
            "Group": {},
            "Teacher": {},
            "Student": {},
            "Subject": {},
            "Grade": {},
        },
    }

    parser = argparse.ArgumentParser(exit_on_error=False, add_help=True)
    parser.add_argument("-a", "--action", choices=PARSE_COMMANDS.keys())
    parser.add_argument(
        "-m",
        "--model",
        choices=list(
            set(
                model
                for model_dict in PARSE_COMMANDS.values()
                for model in model_dict.keys()
            )
        ),
        required=True,
    )

    args, _ = parser.parse_known_args()

    action = args.action
    model = args.model

    if action and model:
        command_args = PARSE_COMMANDS[action][model]
        for arg_short, arg_long in command_args.items():
            parser.add_argument(arg_short, arg_long, type=str, required=True)

    parser.add_argument(
        "-id",
        "--identif",
        required=(
                (action == "update" or action == "delete")
        ),
        nargs="?" if action == "create" else None,
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        required=(action == "update" and model != "Grade")
        or (action == "create" and model != "Grade"),
    )

    return parser.parse_args()

