from sudoku import Sudoku

def main():
    InputFile = open('sudoku.txt','r')

    game_board = list()

    for line in InputFile:
        game_board += [int(i) for i in line.split(',')]
    InputFile.close
    #Close the text file

    #Create the sudoku object
    sudoku = Sudoku(game_board)


    #Print properties for debugging
    print(sudoku.variables)
    print(sudoku.domain)



if __name__ == '__main__':
    main()
    
