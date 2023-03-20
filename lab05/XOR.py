
def XOR(val1, val2):
    return bool(val1) != bool(val2)

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
    test(XOR('kayak', ''), True)
    test(XOR('python', None), True)
    test(XOR(None, None), False)
    test(XOR(0, None), False)
    test(XOR('a', 2), False)


if __name__ == '__main__':
    main()
