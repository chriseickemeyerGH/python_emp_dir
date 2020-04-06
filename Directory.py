
from Employee import Employee


class Directory:

    def __init__(self, directory={}):
        self.directory = directory

    def add_element(self, employee, initial_query=False):  # Employee employee
        key = employee.get_name()
        if key not in self.directory:
            self.directory[key] = employee.get_attrs()
            if not initial_query:
                print("Add successful")
        else:
            print("Employee entry already exists")

    def query_file_data(self, file):  # Employee employee
        for line in file:
            values = line.split("/")
            self.add_element(Employee(
                values[0], values[1], values[2], values[3], values[4], values[5]), True)

    def write_file_data(self, file):
        written_lines = ""
        for (k, v) in self.directory.items():
            line = k + "/" + v
            written_lines += line
        file.write(written_lines)
        return written_lines

    def remove_element(self, name):
        if name in self.directory:
            del self.directory[name]
            print("Entry deleted")
        else:
            self.entry_not_found()

    def print_entry(self, name):
        if name in self.directory:
            print(name + "/" + self.directory[name], end="")
        else:
            self.entry_not_found()

    def edit_entry(self, name, field, update):  # Employee new_employee
        if name in self.directory:
            entry = self.directory[name].split("/")
            tempEmployee = Employee(
                name, entry[0], entry[1], entry[2], entry[3], entry[4])

            fields = ['email', 'phone',
                      'department', 'title', 'education']
            field = field.lower().strip()
            if field in fields:
                method = "tempEmployee.set_{}(update)".format(field)
                exec(method)
                self.directory[name] = tempEmployee.get_attrs()
                print("Entry updated")
            else:
                print("Invalid field entered")
        else:
            self.entry_not_found()

    def get_directory(self):
        return self.directory

    def print_directory(self):
        if len(self.directory) > 0:
            for key in self.directory:
                print(key + "/" + self.directory[key], end="")
        else:
            print("Directory is empty")

    def entry_not_found(self):
        print("Entry does not exist")
