from sudoku import Sudoku


def main():
    InputFile = open('sudoku.txt', 'r')

    game_board = list()

    for line in InputFile:
        game_board += [int(i) for i in line.split(',')]
    InputFile.close
    # Close the text file

    # Create the sudoku object
    sudoku = Sudoku(game_board)

    # Print properties for debugging
    print(sudoku.variables)

    #for x in sudoku.domain:
    #    print(x + ": ", end='')
    #    print(sudoku.domain[x])

    sudoku.create_constraints() #Just for testing right now


if __name__ == '__main__':
    main()
