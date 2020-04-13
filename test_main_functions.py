from main import first_chars
from main import remaining_chars


class TestMainFuncs:

    def test_first_chars(self):
        assert first_chars(4, "EDIT Jane Fonda") == "edit"

    def test_first_chars_two(self):
        assert first_chars(10, "THIS is SOME string") == "this is so"

    def test_remaining_chars(self):
        assert remaining_chars(5, "edit MIKE NEWMAN") == "MIKE NEWMAN"

    def test_remaining_chars_two(self):
        assert remaining_chars(10, "this is a test string to assert") == "test string to assert"
