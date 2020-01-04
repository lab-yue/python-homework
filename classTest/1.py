class TestClass:
    a = 1

    def __init__(self):
        self.b = 2

    @staticmethod
    def test():
        pass


if __name__ == '__main__':
    print("\n".join(dir(TestClass)))
