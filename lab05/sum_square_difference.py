

def get_sum_of_squares(limit_num):
    sum = 0
    for num in range(limit_num):
        sum += num**2
    return sum


def get_square_of_sum(limit_num):
    sum = 0
    for num in range(limit_num):
        sum += num
    return sum**2


def diff():
    sum_of_squares = get_sum_of_squares(100)
    square_of_sums = get_square_of_sum(100)
    return square_of_sums - sum_of_squares 


def main():
    result = diff()
    print('result is: {0}'.format(result))


if __name__ == '__main__':
    main()
