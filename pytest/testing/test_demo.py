def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


class TestDemo:

    def setup_class(self):
        print("TestDemo set up class")

    def teardown_class(self):
        print("Testdemo tear down class")

    def setup(self):
        print("TestDemo set up")

    def teardown(self):
        print("TestDemo tear down")

    def test_demo2(self):
        print("demo2")

    def test_demo3(self):
        print("demo3")