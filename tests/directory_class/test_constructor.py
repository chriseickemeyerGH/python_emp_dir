from src.Directory import Directory


def test_constructor_attrs():
    d = Directory()
    z = Directory(None)
    c = Directory({"key": "value"})
    e = Directory({4: "value here"})

    assert getattr(d, "directory") == {}
    assert getattr(z, "directory") == {}
    assert getattr(c, "directory") == {"key": "value"}
    assert getattr(e, "directory") == {4: "value here"}
