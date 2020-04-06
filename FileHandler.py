

class FileHandler:
    def __init__(self, file_name="directory.txt"):
        self.file_name = file_name

    def get_filename(self):
        return self.file_name

    def read_file(self, directory):  # Directory directory
        try:
            with open(self.file_name, "r") as file:
                directory.query_file_data(file)
                print("Directory file '{}' found. Its data will be used in this application.".format(
                    self.file_name))
        except FileNotFoundError:
            print(
                "The Directory file '{}' does not exist. Add and submit data to create.".format(self.file_name))

    def write_file(self, directory):  # Directory directory
        try:
            with open(self.file_name, "w") as file:
                directory.write_file_data(file)
        except IOError:
            print("Error writing to file")
