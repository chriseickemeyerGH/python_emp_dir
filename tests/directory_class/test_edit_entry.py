from src.Directory import Directory


# def edit_entry(self, name, update=None, field=None):
#     if name in self.directory:
#         entry = self.directory[name].split("/")
#         temp_employee = Employee(
#             name, entry[0], entry[1], entry[2], entry[3], entry[4])
#
#         if field is None:
#             field = input(
#                 "Which field would you like to change? " +
#                 "Fields are 'email', 'phone', 'department', 'title', and 'education'?: ")
#
#         field = field.lower()
#         fields = ['email', 'phone', 'department', 'title', 'education']
#
#         if field in fields:
#             if update is None:
#                 update = input("Enter new {} information: ".format(field))
#
#             exec("temp_employee.set_{}('{}')".format(field, update))
#
#             self.directory[name] = temp_employee.get_attrs()
#             print("Entry updated")
#         else:
#             print("Invalid field entered")
#     else:
#         entry_not_found()

class TestEditEntry:
    def test_name_fail(self, capfd):
        d = Directory({"Rachel Wood": "rachel@yahoo.com/283 482 4929/IT/IT Person/U of A/\n"})
        person = "George Zip"
        d.edit_entry(person, "zipper@gmail.com", "email")

        out, err = capfd.readouterr()

        assert out == "Entry does not exist\n"
        assert person not in getattr(d, "directory")

    def test_name_fail_2(self, capfd):
        d = Directory({"Rachel Wood": "rachel@yahoo.com/283 482 4929/IT/IT Person/U of A/\n"})
        new_rachel = "Rachel WOOD"
        d.edit_entry(new_rachel, "zipper@gmail.com", "email")

        out, err = capfd.readouterr()

        assert out == "Entry does not exist\n"
        assert new_rachel not in getattr(d, "directory")

    def test_field_fail(self, capfd):
        name = "Rachel Wood"
        d = Directory({name: "rachel@yahoo.com/283 482 4929/IT/IT Person/U of A/\n"})
        d.edit_entry(name, "rrr@gmail.com", "email ")

        out, err = capfd.readouterr()

        assert out == "Invalid field entered\n"
        assert name in getattr(d, "directory")

    def test_field_fail_2(self, capfd):
        name = "Rachel Wood"
        d = Directory({name: "rachel@yahoo.com/283 482 4929/IT/IT Person/U of A/\n"})
        d.edit_entry(name, "rrr@gmail.com", "job title")

        out, err = capfd.readouterr()

        assert out == "Invalid field entered\n"
        assert name in getattr(d, "directory")

    def test_success_1(self, capfd):
        name = "Rachel Wood"
        d = Directory({name: "rachel@yahoo.com/283 482 4929/IT/IT Person/U of A/\n"})
        d.edit_entry(name, "IT Manager", "title")

        out, err = capfd.readouterr()
        new_directory = getattr(d, "directory")

        assert out == "Entry updated\n"
        assert new_directory == {name: "rachel@yahoo.com/283 482 4929/IT/IT Manager/U of A/\n"}
        assert name in new_directory

    def test_success_2(self, capfd):
        name = "Rachel Wood"
        d = Directory({name: "rachel@yahoo.com/283 482 4929/IT/IT Person/U of A/\n"})
        d.edit_entry(name, " 555 555 5555 ", "PHONE")

        out, err = capfd.readouterr()
        new_directory = getattr(d, "directory")

        assert out == "Entry updated\n"
        assert new_directory == {name: "rachel@yahoo.com/ 555 555 5555 /IT/IT Person/U of A/\n"}
        assert name in new_directory
