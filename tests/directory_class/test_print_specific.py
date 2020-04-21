from src.Directory import Directory


class TestPrintSpecificMethods:

    # ----------- Test print_entry() -----------
    def test_print_entry_success(self, capfd):
        name = "Megan Bloom"
        d = Directory({name: "p1@gmail.com/555 294 4929/IT/IT Director/U of Y/\n"})
        d.print_entry(name)

        out, err = capfd.readouterr()

        assert name in getattr(d, "directory")
        assert out == name + "/p1@gmail.com/555 294 4929/IT/IT Director/U of Y/\n"

    def test_print_entry_fail(self, capfd):
        person = "George Zip"
        d = Directory({"Megan Bloom": "p1@gmail.com/555 294 4929/IT/IT Director/U of Y/\n"})
        d.print_entry(person)

        out, err = capfd.readouterr()

        assert person not in getattr(d, "directory")
        assert out == "Entry does not exist\n"

    # ----------- Test print_length() ------------

    def test_print_length_multiple(self, capfd):
        directory = {
            "George Zipper": "p1@gmail.com/555 294 4929/IT/IT Director/U of Y/\n",
            "Megan Bloom": "bloomer@gmail.com/204 294 4919/Marketing/Marketing Doctor/U of Q/\n"
        }
        d = Directory(directory)
        d.print_length()
        out, err = capfd.readouterr()

        assert out == "2 entries in directory\n"
        assert len(getattr(d, "directory")) == 2

    def test_print_length_one(self, capfd):
        directory = {"George Zipper": "p1@gmail.com/555 294 4929/IT/IT Director/U of Y/\n"}
        d = Directory(directory)
        d.print_length()
        out, err = capfd.readouterr()

        assert out == "1 entry in directory\n"
        assert len(getattr(d, "directory")) == 1

    def test_print_length_none(self, capfd):
        d = Directory()
        d.print_length()
        out, err = capfd.readouterr()

        assert out == "0 entries in directory\n"
        assert len(getattr(d, "directory")) == 0

        # ----------- Test print_directory() --------------

    def test_print_directory_empty(self, capfd):
        d = Directory()
        d.print_directory()
        out, err = capfd.readouterr()

        assert out == "Directory is empty\n"
        assert len(getattr(d, "directory")) == 0

    def test_print_directory_multiple(self, capfd):
        directory = {
            "George Zipper": "p1@gmail.com/555 294 4929/IT/IT Director/U of Y/\n",
            "Megan Bloom": "bloomer@gmail.com/204 294 4919/Marketing/Marketing Doctor/U of Q/\n",
            "Mike Whiff": "mike@gmail.com/4929428582/Sales/Sales Person/U of U/\n"
        }
        d = Directory(directory)
        d.print_directory()

        out, err = capfd.readouterr()

        dir_var = getattr(d, "directory")

        assert len(dir_var) > 0
        assert len(dir_var) == 3
        assert out == "George Zipper/p1@gmail.com/555 294 4929/IT/IT Director/U of Y/\n" + \
               "Megan Bloom/bloomer@gmail.com/204 294 4919/Marketing/Marketing Doctor/U of Q/\n" + \
               "Mike Whiff/mike@gmail.com/4929428582/Sales/Sales Person/U of U/\n"
