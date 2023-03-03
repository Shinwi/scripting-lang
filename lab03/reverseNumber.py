# exc source: https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=EnPy3.20120815j

# Write a function that receives a whole number (integer) and returns its reverse as a whole number.

# Examples: 1977 →7791; 12568 → 86521.

# (We can suppose that the original number doesn't end with 0).

def reverseNumber(num):
    stringNum = str(num)
    stringNum = stringNum[::-1]
    return int(stringNum)


def test(got, expected):
    if got == expected:
        prefix = 'OK'
    else:
        prefix = 'X'
    
    print('{p} got: {g} | expected: {e}'.format(p=prefix, g=got, e=expected))



def main():
    test(reverseNumber(1005), 5001)
    test(reverseNumber(2023), 3202)
    test(reverseNumber(2064), 4602)
    test(reverseNumber(54321), 12345)


#############################################################################

if __name__ == '__main__':
    main()