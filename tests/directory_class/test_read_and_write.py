from src.Directory import Directory


class TestReadWrite:
    def test_query_file(self, tmpdir):
        d = Directory()

        file = tmpdir.mkdir("dir").join("tester.txt")
        file.write("Mike Jones/mike@gmail.com/383 482 4828/Marketing/Marketing Coordinator/U of A/\n")
        file_read_ref = open(file, "r")

        d.query_file_data(file_read_ref)
        assert getattr(d, "directory") == {
            "Mike Jones": "mike@gmail.com/383 482 4828/Marketing/Marketing Coordinator/U of A/\n"}

    def test_query_file_two(self, tmpdir):
        d = Directory()

        file = tmpdir.mkdir("dir").join("tester.txt")

        file.write(
            "Mike Jones/mike@gmail.com/383 482 4828/Marketing/Marketing Coordinator/U of A/\n" +
            "George Zip/zipper@yahoo.com/394 4959 2949/IT/IT Director/U of Z/\n")
        file_read_ref = open(file, "r")

        d.query_file_data(file_read_ref)
        assert getattr(d, "directory") == {
            "Mike Jones": "mike@gmail.com/383 482 4828/Marketing/Marketing Coordinator/U of A/\n",
            "George Zip": "zipper@yahoo.com/394 4959 2949/IT/IT Director/U of Z/\n"
        }

    def test_write_data(self, tmpdir):
        dir_vals = {"George Zip": "george@yahoo.com/438 283 5820/IT/IT Person/U of O/\n"}
        d = Directory(dir_vals)

        file = tmpdir.mkdir("sub").join("tester.txt")
        data = d.write_file_data()
        file.write(data)

        assert data == "George Zip/george@yahoo.com/438 283 5820/IT/IT Person/U of O/\n"
        assert file.read() == data

    def test_write_2(self, tmpdir):
        directory = {"Mike Smith": "smith@gmail.com/293 294 2914/Marketing/Marketing Coordinator/U of MN/\n",
                     "George Williams": "georgie@gmail.com/555 509 9043/IT/IT Person/U of MZ/\n"}
        d = Directory(directory)

        fake_file = tmpdir.mkdir("sub").join("tester.txt")
        data = d.write_file_data()
        fake_file.write(data)

        assert data == "Mike Smith/smith@gmail.com/293 294 2914/Marketing/Marketing Coordinator/U of MN/\n" + \
               "George Williams/georgie@gmail.com/555 509 9043/IT/IT Person/U of MZ/\n"

        assert fake_file.read() == data
