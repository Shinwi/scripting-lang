
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples_of_3_or_5():
    """Returns the sum all the multiples of 3 or 5 below 1000"""
    return sum([ i for i in list(range(1000 + 1)) if i%5 == 0 or i%3 == 0])


def main():
    result =  sum_of_multiples_of_3_or_5() 
    print('\nThe sum of all multiples of 3 and 5 under 100 is: {0}'.format(result))


if __name__ == "__main__":
    main()