'''
testing exceptions - caught vs raised
chatterbox functions? - if exists: return val else: print something --- balancing these
structuring file class- how to handle file actions separately
type checking - benefits with objects
keep count instead of determing length of dict everytime
'''
from Employee import Employee
from FileHandler import FileHandler
from Directory import Directory


def print_directions():
    print("""\nCommands:
"view directory"-> print entire directory
"view/edit/add/delete enter_employee_name_here"-> print/edit/add/delete employee listing
"quit"-> end session and write to file
"help"-> print commands (this list)
""")


def enter_command():
    val = input("Enter command: ")
    return val.lower()


def first_chars(index_num, val):
    return val[:index_num]


def remaining_chars(index_num, val):
    return val[index_num:]


def add_field(field):
    val = input("Enter {}: ".format(field))
    return val


def main():
    print("Starting session...")

    queried_file = FileHandler()
    collection = Directory()
    queried_file.read_file(collection)
    print_directions()

    val = enter_command()

    while val != "quit":
        if val == "view directory":
            collection.print_directory()

        elif first_chars(5, val) == "view ":
            collection.print_entry(remaining_chars(5, val))

        elif first_chars(5, val) == "edit ":
            name = remaining_chars(5, val)
            field = input(
                "Which field would you like to change? Fields are 'email', 'phone', 'department', 'title', and 'education'?\n")
            update = input("Enter new information: ")
            collection.edit_entry(name, field, update)

        elif first_chars(4, val) == "add ":

            name = remaining_chars(4, val)
            email = add_field("email")
            phone = add_field("phone")
            department = add_field("department")
            title = add_field("title")
            education = add_field("education")

            new_employee = Employee(name, email,
                                    phone, department, title, education)

            collection.add_element(new_employee)

        elif first_chars(7, val) == "delete ":
            collection.remove_element(remaining_chars(7, val))

        elif val == "help":
            print_directions()

        else:
            print("Invalid command entered")

        val = enter_command()

    print("Writing to file...")

    write__ref = FileHandler()
    write__ref.write_file(collection)

    print("Session ended")


main()
