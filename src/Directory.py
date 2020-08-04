from Employee import Employee


def entry_dne():
    print("Entry does not exist")


class Directory:

    # https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments

    def __init__(self, directory=None):
        if directory is None:
            directory = {}

        self.directory = directory

    def query_file_data(self, file):
        for line in file:  # open(file_name, "r")
            values = line.split("/")
            self.add_employee(Employee(
                values[0], values[1], values[2], values[3], values[4], values[5]), True)

    # video example
    def write_file_data(self, file=None):  # open(file_name, "w")
        total_data = ""
        for key in self.directory:
            total_data += (key + "/" + self.directory[key])
        if file:
            file.write(total_data)
        else:
            return total_data

    def add_employee(self, employee, initial_query=False):  # Employee employee
        key = employee.get_name()
        if key not in self.directory:
            self.directory[key] = employee.stringify_attrs()
            if not initial_query:
                print("Add successful")
        else:
            print("Employee entry already exists")

    # video example
    def remove_employee(self, name):
        if name in self.directory:
            del self.directory[name]
            print("Entry deleted")
        else:
            entry_dne()

    # video example
    def edit_entry(self, name, update=None, field=None):
        if name in self.directory:
            entry = self.directory[name].split("/")
            temp_employee = Employee(
                name, entry[0], entry[1], entry[2], entry[3], entry[4])

            if field is None:
                field = input(
                    "Which field would you like to change? " +
                    "Fields are 'email', 'phone', 'department', 'title', and 'education': ")

            field = field.lower()
            fields = ['email', 'phone', 'department', 'title', 'education']

            if field in fields:
                if update is None:
                    update = input("Enter new {} information: ".format(field))

                exec("temp_employee.set_{}('{}')".format(field, update))

                self.directory[name] = temp_employee.stringify_attrs()
                print("Entry updated")
            else:
                print("Invalid field entered")
        else:
            entry_dne()

    # video example
    def print_entry(self, name):
        if name in self.directory:
            print(name + "/" + self.directory[name], end="")
        else:
            entry_dne()

    def print_length(self):
        length = len(self.directory)

        if length == 1:
            entry_string = "entry"
        else:
            entry_string = "entries"

        print(length, entry_string, "in directory")

    def print_directory(self):
        if len(self.directory) > 0:
            for key in self.directory:
                print(key + "/" + self.directory[key], end="")
        else:
            print("Directory is empty")
