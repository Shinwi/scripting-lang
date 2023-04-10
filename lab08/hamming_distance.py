
def hamming_distance(a: str, b: str):
    """Returns an integer which represents the hamming distance between two strings"""
    
    if len(a) != len(b):
        return 'Given strings have different lengths. The hamming distance cannot be calculated.'
    
    common_letters = []
    list_a, list_b = list(a), list(b)

    for c in list_a:
        if c in list_b:
            common_letters.append(c)
            list_b.remove(c)

    return len(a) - len(common_letters)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
    test(hamming_distance('toned', 'roses'), 3)
    test(hamming_distance('axxaxxa', 'ayyayya'), 4)
    test(hamming_distance('taco', 'goat'), 1)
    test(hamming_distance('start', 'tames'), 2)


if __name__ == "__main__":
    main()
