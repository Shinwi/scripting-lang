
def remove_comments_from_file(fileName):
    with open(fileName, 'r') as inputFile, open('string1_clean.py', 'w') as outputFile:
        inputLines = inputFile.readlines()
        for line in inputLines:
            if not line.strip().startswith('#'):
                outputFile.write(line)


def main():
    remove_comments_from_file('string1.py')


if __name__ == '__main__':
    main()
