# exc source: https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=EnPy3.20120815e

# 1- Trivial method
def isPalindrom(s):
    return s == s[::-1]


# 2 - Iterative method. You are not allowed to make a copy of the string.
def iterativeIsPalindrom(s):
    n = len(s)
    for i in range(len(s)):
        if s[i] != s[n - 1 - i]:
            return False
        if i >= n//2:
            break
    return True


# 3 - Recursive method. Just to practice recursion too.
def recursiveIsPalindrom(s):
    firstChar = s[0]
    lastChar = s[-1]
    
    if (len(s) <= 3):
        return firstChar == lastChar
    
    newS = s[1:-1]
    return recursiveIsPalindrom(newS)


# Stealing this cool testing method
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
    print('Trivial Method:')
    test(isPalindrom('tacos'), False)
    test(isPalindrom('Bimo'), False)
    test(isPalindrom('tacocat'), True)
    test(isPalindrom('kayak'), True)
    print('\nIterative Methods:')
    test(iterativeIsPalindrom('tacos'), False)
    test(iterativeIsPalindrom('Bimo'), False)
    test(iterativeIsPalindrom('tacocat'), True)
    test(iterativeIsPalindrom('kayak'), True)
    print('\nRecursive Method:')
    test(recursiveIsPalindrom('tacos'), False)
    test(recursiveIsPalindrom('Bimo'), False)
    test(recursiveIsPalindrom('tacocat'), True)
    test(recursiveIsPalindrom('kayak'), True)

if __name__ == '__main__':
    main()