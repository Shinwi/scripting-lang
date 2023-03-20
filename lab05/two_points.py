import math


def distance(p1, p2):
    return math.sqrt( (p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('The distance between the two points:', distance(p1, p2))

############################################################################

if __name__ == "__main__":
    main()