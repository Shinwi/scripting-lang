

def main():
    with open('inputNumberFile.txt', 'r') as inputFile:
        lines = inputFile.readlines()
        integer_list_of_lines = [int(line.replace('\n','')) for line in lines]
        total_sum = sum(integer_list_of_lines)
        print('The sum of the first 10 digits are: {answer}'.format(answer = str(total_sum)[:10]))

if __name__ == '__main__':
    main()