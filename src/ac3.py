from sudoku import Sudoku

def AC3(board):
    # queue of arcs (initially all constraints)
    arc_queue = list(board.constraints)
    while arc_queue:
        arc1,arc2 = arc_queue.pop(0)
        if revise(board, arc1, arc2):
            # check if D1 is = 0, which means no solution
            if not board.domain[arc1]:
                return False
            # else for each neighbour of
            for neighbours in board.neighbours[arc1]:
                # will skip if x2 is found as we do not need this value appended
                if neighbours == arc2:
                    continue
                temp_list = [neighbours, arc1]
                arc_queue.append(temp_list)
    return True

# takes board, current_arc[0](x1) and current_arc[1](x2) as parameters
# returns true iff domain x1 is revised

def revise(board, x1, x2):
    revised = False
    # check each value in the domain of x1
    for x in board.domain[x1]:
        if not any ([x!=y for y in board.domain[x2]]):
            board.domain[x1].remove(x)   # delete from domain if true
            revised = True
    return revised

def backtrack(csp):


def main():
    InputFile = open('sudoku.txt')

    game_board = list()

    for line in InputFile:
        game_board += [int(i) for i in line.split(',')]
    # Close the text file
    InputFile.close

    # Create the sudoku object
    board = Sudoku(game_board)

    if not AC3(board):
        print("No Solution Found")
    else:
        print("Solution Found")
        # print(board.domain)
        print("|", end="")
        count = 0
        row = 0
        for x in board.domain:
            if count == 9:
                count = 0
                print()  # starts new line
                row += 1
                if row == 3 or row == 6:
                    print()
                print('|', end='')
            if count == 3 or count == 6:
                print("  |", end="")
            print("{}|".format(board.domain[x][0]), end="")
            count += 1

if __name__ == '__main__':
    main()



