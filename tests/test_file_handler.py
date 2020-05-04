from src.FileHandler import FileHandler


class TestFileHandler:

    def test_file_name(self):
        f = FileHandler("")
        f2 = FileHandler("some_file.py")

        assert getattr(f, "file_name") == "directory.txt"
        assert getattr(f2, "file_name") == "some_file.py"

    def test_read_file_found(self, tmpdir, capfd):
        file = tmpdir.mkdir("sub").join("tester.txt")
        file.write("")
        f = FileHandler(file)
        f.read_file()

        out, err = capfd.readouterr()
        assert out == "File '{}' found. Its data will be used in this application.\n".format(file)

    def test_read_file_not_found(self, tmpdir, capfd):
        file = tmpdir.mkdir("sub").join("file_dne.txt")

        f = FileHandler(file)
        f.read_file()

        out, err = capfd.readouterr()
        assert out == "File '{}' does not exist. Add and submit data to create it.\n".format(file)

    def test_write_file_success(self, tmpdir, capfd):
        file = tmpdir.mkdir("sub").join("test.txt")

        f = FileHandler(file)
        f.write_file()

        out, err = capfd.readouterr()
        assert out == "Data write to '{}' successful\n".format(file)

    def test_write_file_fail(self, capfd):
        f = FileHandler("some_file.txt")
        f.write_file(write_fail=True)  # trigger exception to be caught

        out, err = capfd.readouterr()
        assert out == "Error writing to '{}'\n".format(getattr(f, "file_name"))
