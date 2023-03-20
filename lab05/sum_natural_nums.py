# variation 2

# Take the natural numbers from 1 to 100 (included), and calculate the sum of the digits in the numbers. For instance, the sum of the digits in the numbers [10, 11, 12] is 6 (1+0+1+1+1+2=6).

def digits_sum(number):
    sum = 0
    strList = list(str(number))
    for c in strList:
        sum += int(c)
    return sum


def sum_of_digits_in_number():
    total_sum = 0
    for i in range(1,100+1):
        if i < 11:
            total_sum += i
        else:
            total_sum += digits_sum(i)
    return total_sum

def main():
   result = sum_of_digits_in_number()
   print('result: {0}'.format(result))


############################################################################

if __name__ == "__main__":
    main()