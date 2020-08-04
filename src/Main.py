
from Employee import Employee
from FileHandler import FileHandler
from Directory import Directory


def print_directions():
    print("""\nCommands:
"view directory"-> view entire directory
"entry count"-> view number of entries in directory
"view/edit/add/delete enter_employee_name_here"-> view/edit/add/delete employee listing
"quit"-> end session and write to file
"help"-> view commands (this list)
""")


def enter_command():
    val = input("Enter command: ")
    return val


def first_chars(index_num, val):
    return val[:index_num].lower()


def remaining_chars(index_num, val):
    return val[index_num:]


def add_field(field):
    val = input("Enter employee {}: ".format(field))
    return val


def main():
    print("Starting session...")
    file_name = input("Enter name of file to read and write to (press 'Enter' to use default — 'directory.txt': ")

    queried_file = FileHandler(file_name)
    collection = Directory()
    queried_file.read_file(collection)
    print_directions()

    val = enter_command()

    while val.lower() != "quit":
        if val.lower() == "view directory":
            collection.print_directory()

        elif val.lower() == "entry count":
            collection.print_length()

        elif first_chars(5, val) == "view ":
            collection.print_entry(remaining_chars(5, val))

        elif first_chars(5, val) == "edit ":
            name = remaining_chars(5, val)
            collection.edit_entry(name)

        elif first_chars(4, val) == "add ":

            name = remaining_chars(4, val)
            email = add_field("email")
            phone = add_field("phone")
            department = add_field("department")
            title = add_field("title")
            education = add_field("education")

            new_employee = Employee(name, email,
                                    phone, department, title, education)

            collection.add_employee(new_employee)

        elif first_chars(7, val) == "delete ":
            collection.remove_employee(remaining_chars(7, val))

        elif val == "help":
            print_directions()

        else:
            print("Invalid command entered")

        val = enter_command()

    write_ref = FileHandler(file_name)
    write_ref.write_file(collection)

    print("Session ended")


if __name__ == "__main__":
    main()
