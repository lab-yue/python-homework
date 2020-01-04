import numbers


class Sqr:
    def __init__(self, x):
        if (isinstance(x, numbers.Number) and not isinstance(x, bool)):
            self._x = None
        else:
            self._x = x

    def getX(self):
        return self._x

    def setX(self, x):
        self._x = x

    def getSqrX(self):
        return self._x ** 2


if __name__ == '__main__':

    # prepare
    value = 5
    s = Sqr(value)

    # test getX and getSqrX
    assert s.getX() == value
    assert s.getSqrX() == value ** 2

    # test setX
    s.setX(value ** 2)
    assert s.getX() == value ** 2
    assert s.getSqrX() == value ** 4

    print('ok')
