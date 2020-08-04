class FileHandler:
    def __init__(self, file_name):
        if file_name == "":
            self.file_name = "directory.txt"
        else:
            self.file_name = file_name

    def read_file(self, directory=None):  # Directory directory
        try:
            with open(self.file_name, "r") as file:
                if directory:
                    directory.query_file_data(file)
                print("File '{}' found. Its data will be used in this application.".format(
                    self.file_name))

        except FileNotFoundError:
            print(
                "File '{}' does not exist. Add and submit data to create it.".format(self.file_name))

    # video example
    def write_file(self, directory=None, write_fail=None):  # Directory directory
        try:
            if write_fail:
                raise OSError
            with open(self.file_name, "w") as file:
                if directory:
                    directory.write_file_data(file)
            print("Data write to '{}' successful".format(self.file_name))

        except OSError:
            print("Error writing to '{}'".format(self.file_name))
