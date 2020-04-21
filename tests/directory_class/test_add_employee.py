from src.Directory import Directory
from src.Employee import Employee


class TestAddEmployee:
    def test_add_employee_single_add(self, capfd):
        d = Directory()
        emp1 = Employee("Chris Williams", "test@gmail.com", "923 392 3948", "IT", "IT Manager", "U of A")
        d.add_employee(emp1)

        out, err = capfd.readouterr()

        assert out == "Add successful\n"
        assert getattr(d, "directory") == {"Chris Williams": "test@gmail.com/923 392 3948/IT/IT Manager/U of A/\n"}

    def test_add_employee_add_another(self, capfd):
        directory = {"Joe Person": "google@hotmail.com/555 528 1394/Marketing/Marketing Manager/College of Math/\n"}
        d = Directory(directory)
        emp_add = Employee("Will Meyers", "fred@gmail.com", "495 582 5828", "IT", "IT Admin", "U of Q")
        d.add_employee(emp_add)

        out, err = capfd.readouterr()

        assert out == "Add successful\n"
        assert getattr(d, "directory") == {
            "Joe Person": "google@hotmail.com/555 528 1394/Marketing/Marketing Manager/College of Math/\n",
            "Will Meyers": "fred@gmail.com/495 582 5828/IT/IT Admin/U of Q/\n"}

    def test_add_employee_initial_query(self):
        directory = {"Joe Person": "google@hotmail.com/555 528 1394/Marketing/Marketing Manager/College of Math/\n",
                     "Rachel Matthews": "red@yahoo.com/934 485 2058/IT/IT Manager/U of Z/\n"}
        d = Directory(directory)

        new_emp = Employee("Roger Name", "hello@gmail.com", "920 482 4820", "Sales", "Sales Rep", "U of Webster")
        d.add_employee(new_emp, True)

        current_dir = getattr(d, "directory")
        assert "Joe Person" in current_dir and "Rachel Matthews" in current_dir and "Roger Name" in current_dir

    def test_add_employee_already_in_dir(self, capfd):
        name = "Joe Person"
        directory = {name: "google@hotmail.com/555 528 1394/Marketing/Marketing Manager/College of Math/\n"}
        d = Directory(directory)

        emp = Employee(name, "jibberish@google.com", "939 29492 49294", "IT", "IT Person", "College of OHIO")
        d.add_employee(emp)

        out, err = capfd.readouterr()

        assert name in getattr(d, "directory")
        assert out == "Employee entry already exists\n"
