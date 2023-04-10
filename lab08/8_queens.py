
def draw_chessboard(lst):
    """Draws a chessboard and represents the Queen in the given positions"""
    board_size = len(lst)

    if board_size != 8:
        print('Cannot print a chessboard! list of positions must have 8 elements.')
        return
    
    print('+', '-'*15, '+')
    for i in range(board_size):
        row = []
        for j in range(board_size):
            if (j == 8 - lst[i] - 1):
                row.append('Q')
            else:
                row.append('.')
        print('| ' + ' '.join(row) + ' |')
    print('+', '-'*15, '+')


def main():
    draw_chessboard([0,4,7,5,2,6,1,3])


if __name__ == "__main__":
    main()
