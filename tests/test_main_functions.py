from src.main import first_chars
from src.main import remaining_chars


class TestMainFuncs:

    def test_first_chars(self):
        assert first_chars(4, "EDIT Jane Fonda") == "edit"
        assert first_chars(10, "THIS is SOME string") == "this is so"

    def test_remaining_chars(self):
        assert remaining_chars(5, "edit MIKE NEWMAN") == "MIKE NEWMAN"
        assert remaining_chars(6, "this is a test string to assert") == "s a test string to assert"
