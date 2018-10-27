from sudoku import Sudoku

def AC3(board):
    # queue of arcs (initially all constraints)
    arc_queue = board.constraints
    while arc_queue:
        current_arc = arc_queue.pop()
        if revise(board, current_arc[0], current_arc[1]):
            # check if D1 is = 0, which means no solution
            if not board.domain[current_arc[0]]:
                return False
            # else for each neighbour of
            for neighbours in board.neighbours[current_arc[0]]:
                # will skip if x2 is found as we do not need this value appended
                if neighbours == current_arc[1]:
                    continue
                temp_list = [neighbours, current_arc[0]]
                arc_queue.append(temp_list)
    return True


# takes board, current_arc[0](x1) and current_arc[1](x2) as parameters
# returns true iff domain x1 is revised

def revise(board, x1, x2):
    revised = False
    # check each value in the domain of x1
    for d in board.domain[x1]:
        if d in board.domain[x2]:
            del[d]  # delete from domain if true
        revised = True
    return revised

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
    
    # board.create_neighbours()

    if not AC3(board):
        print("No Solution Found")
    else:
        Sudoku.print_sudoku(board)




if __name__ == '__main__':
    main()




