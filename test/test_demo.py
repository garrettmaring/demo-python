from engi_python_demo.calc import add, sub


def test_ok():
    assert add(5, 5) == 10


def test_fail():
    assert sub(10, 5) == 5
