from sudoku import Sudoku


def AC3(board):
    # queue of arcs (initially all constraints)
    arc_queue = list(board.constraints)
    while arc_queue:
        arc1, arc2 = arc_queue.pop(0)
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
        if not any([x != y for y in board.domain[x2]]):
            board.domain[x1].remove(x)   # delete from domain if true
            revised = True
    return revised


def backtrack(assignments, board):
    if len(assignments) == len(board.variables):
        return assignments
    currentVar = minimum_remaining_values(assignments, board)
    #for v in least_constraining_value(currentVar, board):
        #if isConsistent(assignments,currentVar, v, board):


def define_assigned_vars(board):
    assigned = dict()
    for x in board.variables:
        if len(board.domain[x]) == 1:
            assigned[x] = board.domain[x][0]
    return assigned


def minimum_remaining_values(assignments, board):
    unassigned = list()
    for x in board.variables:
        if x not in assignments:
            unassigned.append(x)
    min_var = min(unassigned, key=lambda var: len(board.domain[var]))
    return min_var


def least_constraining_value(var, board):
    if len(board.domain[var]) == 1:
        return board.domain[var]
    sorted_domain = sorted(board.domain[var], key=lambda v: constraints(var, v, board))
    return sorted_domain


def constraints(var, val, board):
    constraints = 0
    for x in board.neighbours[var]:
        if len(board.domain[x]) > 1:
            if x in board.domain[x]:
                constraints += 1
    return constraints


def isConsistent(assignments, var, val, board):
    consistent = True
    for key in assignments:
        if assignments[key] == val:
            if key in board.neighbours[var]:
                consistent = False
    return consistent


def assign(assignments, var, val, board):

    assignments[var] = val
    board.forward_check(assignments, var, val)


def unassign(assignments, var, board):

    if var in assignments:
        for(D, v) in board.updated[var]:
            board.domain[D].append(v)

        board.updated = []
        del assignments[var]


def forward_check(board, var, value, assignment):
    for neighbour in board.neighbours:
        if neighbour not in assignment:
            if value in board.domain[neighbour]:
                board.domain[neighbour].remove(value)
                board.updated[var].append((neighbour, value))

def main():
    InputFile = open('sudoku.txt')

    game_board = list()

    for line in InputFile:
        game_board += [int(i) for i in line.split(',')]
    # Close the text file
    InputFile.close

    # Create the sudoku object
    board = Sudoku(game_board)

    if AC3(board):
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
    else:
        assigned = define_assigned_vars(board)



if __name__ == '__main__':
    main()



