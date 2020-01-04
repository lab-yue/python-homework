def lerp(a, b, t):
    try:
        if 0 <= t <= 1:
            ty = a[1] + (b[1] - a[1]) * (t - a[0]) / (b[0] - a[0])
            return (t, ty), None
        else:
            raise ValueError
    except TypeError:
        return -1, "parameter is not a number"
    except ValueError:
        return -1, "t is out of range"
    except ZeroDivisionError:
        return -1, "ax == bx"


if __name__ == '__main__':
    assert lerp((0, 0), (1, 1), 0)[0] == (0, 0)
    assert lerp((0, 0), (1, 1), 1)[0] == (1, 1)
    assert lerp((0, 0), (1, 1), .5)[0] == (.5, .5)
    assert lerp(("0", "0"), ("0", "0"), 0)[1] == "parameter is not a number"
    assert lerp((0, 0), (1, 1), 2)[1] == "t is out of range"
    assert lerp((0, 0), (0, 0), 0)[1] == "ax == bx"
