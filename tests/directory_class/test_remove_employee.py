from Directory import Directory


class TestRemoveEmployee:
    # video example
    def test_remove_success1(self, capfd):
        emp_remove = "Jason Jones"
        directory = {emp_remove: "jj@gmail.com/382 284 4891/IT/IT Person/U of K"}
        d = Directory(directory)
        d.remove_employee(emp_remove)

        out, err = capfd.readouterr()
        current_dir = getattr(d, "directory")

        assert emp_remove not in current_dir
        assert current_dir == {}
        assert out == "Entry deleted\n"

    def test_remove_success2(self, capfd):
        emp_remove = "Lala Woods"
        directory = {"George Smith": "ggg@gmail.com/294 592 5929/Sales/Sales Admin/U of I/\n",
                     emp_remove: "lala@yahoo.com/628 195 5829/Marketing/Marketing Manager/U of R/\n"}
        d = Directory(directory)
        d.remove_employee(emp_remove)

        out, err = capfd.readouterr()
        current_dir = getattr(d, "directory")

        assert emp_remove not in current_dir
        assert current_dir == {"George Smith": "ggg@gmail.com/294 592 5929/Sales/Sales Admin/U of I/\n"}
        assert out == "Entry deleted\n"

    def test_remove_failure(self, capfd):
        directory = {"Jason Jones": "jj@gmail.com/382 284 4891/IT/IT Person/U of K"}
        d = Directory(directory)

        fake_emp = "Joe Green"
        d.remove_employee(fake_emp)

        out, err = capfd.readouterr()
        current_dir = getattr(d, "directory")

        assert fake_emp not in current_dir
        assert out == "Entry does not exist\n"
