from prettytable import PrettyTable


def pretty_output(columns):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                entity_name = func.__name__.split("_")[1].capitalize()
                table = PrettyTable(columns)

                if "list" in func.__name__:
                    if not result:
                        print(f"{entity_name} table is empty")
                    else:
                        for item in result:
                            table.add_row(item)
                        print(table)
                elif "create" in func.__name__:
                    if result:
                        print(f"{entity_name} created successfully")
                        table.add_row(result)
                        print(table)
                    else:
                        print(f"No {entity_name} created")
                elif "update" in func.__name__:
                    if result:
                        print(f"{entity_name} update successfully.")
                        table.add_row(result)
                        print(table)
                    else:
                        print(f"No {entity_name} updated")
                elif "delete" in func.__name__:
                    if result:
                        print(f"{entity_name} was deleted successfully.")
                        table.add_row(result)
                        print(table)
                    else:
                        print("Error occurred.")
                else:
                    print(f"Invalid function: {func.__name__}")
            except AttributeError as e:
                print(f"Error: {e}")

        return wrapper

    return decorator
