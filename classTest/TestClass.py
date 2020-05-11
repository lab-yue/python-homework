class TestClass:

    def __init__(self, num: int):
        self.A = num

    def doubleA(self):
        return self.A * 2


if __name__ == '__main__':
    t = TestClass(2)
    assert t.doubleA() == 4

