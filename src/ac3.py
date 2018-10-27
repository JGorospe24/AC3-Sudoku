from sudoku import Sudoku


def main():
    InputFile = open('sudoku.txt')

    game_board = list()

    for line in InputFile:
        game_board += [int(i) for i in line.split(',')]
    # Close the text file
    InputFile.close

    # Create the sudoku object
    board = Sudoku(game_board)

    # Print properties for debugging
    # print(board.variables)
    # or x in board.domain:
    #   print(x + ": ", end='')
    #    print(board.domain[x])
    # board.create_constraints() #Just for testing right now


if __name__ == '__main__':
    main()
