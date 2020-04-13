from Employee import Employee


class TestEmployee:

    def test_getters(self):
        e = Employee("Joe Namath", "joe@gmail.com", "392 493 4939", "Marketing", "Marketing Manager", "U of Minnesota")

        assert e.get_name() == "Joe Namath"
        assert getattr(e, "name") == "Joe Namath"
        assert getattr(e, "email") == "joe@gmail.com"
        assert getattr(e, "phone") == "392 493 4939"
        assert getattr(e, "department") == "Marketing"
        assert getattr(e, "title") == "Marketing Manager"
        assert getattr(e, "education") == "U of Minnesota"

    def test_setters(self):
        e = Employee("Joe Namath", "joe@gmail.com", "392 493 4939", "Marketing", "Marketing Manager", "U of Minnesota")

        e.set_name("Mike Jones")
        e.set_email("mike@gmail.com")
        e.set_phone("555 999 3939")
        e.set_department("IT")
        e.set_title("Engineer")
        e.set_education("U of A")

        assert getattr(e, "name") == "Mike Jones"
        assert getattr(e, "email") == "mike@gmail.com"
        assert getattr(e, "phone") == "555 999 3939"
        assert getattr(e, "department") == "IT"
        assert getattr(e, "title") == "Engineer"
        assert getattr(e, "education") == "U of A"

    def test_attributes_string(self):
        e = Employee("Joe Namath", "joe@gmail.com", "392 493 4939", "Marketing", "Marketing Manager", "U of Minnesota")
        d = Employee("Chris Jones", "chris@yahoo.com", "(555) 392 5828", "Sales", "Sales Associate",
                     "University of Cambridge")

        assert e.get_attrs() == "joe@gmail.com/392 493 4939/Marketing/Marketing Manager/U of Minnesota/\n"
        assert d.get_attrs() == "chris@yahoo.com/(555) 392 5828/Sales/Sales Associate/University of Cambridge/\n"
