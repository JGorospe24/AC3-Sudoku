characters = 'ABCDEFGHI'
numbers = '123456789'

# These two global variables will be used to permutate and index the game board
# Example: A1, A2, A3,..,B1,B2,B3,...

# Sudoku Class
# Creates an 9x9 board of 81 tiles


class Sudoku:

    def __init__(self, new_board):
        self.variables = list()
        self.domain = dict()
        self.init_game(new_board)
        self.constraints = list()

    def init_game(self, new_board):
        self.create_variables(numbers, characters)
        self.populate_domain(new_board)

    # Populates the domain of all the tiles and sets the domain of already populated tiles from new_board as the value itself
    # Populates the domain of all the tiles and sets the domain of already populated tiles from new_board as the value itself
    def populate_domain(self, new_board):
        tile_count = 0
        letter = characters[0]
        letter_p = 0
        for x in new_board:
            if (x == 0):
                self.domain[letter + str((tile_count % 9) + 1)] = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]
            else:
                self.domain[letter + str((tile_count % 9) + 1)] = [x]

            tile_count += 1
            if (tile_count % 9) == 0:
                if letter_p < 8:
                    letter_p += 1
                    letter = characters[letter_p]

    # Output:
    # A1: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    # A2: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    # A3: [3],
    # A4: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    # A5: [2],
    # A6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    # A7: [6]

    def create_variables(self, numbers, characters):

        # Creates an empty list which will be populated by the tiles of the board

        for char in characters:
            for num in numbers:
                self.variables.append(char + num)

            # Returns
            # ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
        # 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 
        # 'C1', 'C2', 'C3','C4', 'C5', 'C6', 'C7', 'C8', 'C9', 
        # 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 
        # 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 
        # 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 
        # 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 
        # 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 
        # 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
        
    def create_constraints(self):
        rows = list()
        columns = list()
        
        # create row constraints
        for character in characters:
            temp = list()
            
            for number in numbers:
                
                temp.append(character+number)

            rows.append(temp)
        
        self.constraints.append(rows)
        # testing 
        for row in rows:
            print(row)
            print("One Row") #Testing line
        
        # create column constraints
        print("done rows") #Testing line
        for number in numbers:
            temp = list()
            
            for character in characters:
                
                temp.append(character+number)
                #print(number,character)
                
            columns.append(temp)
        
        for column in columns:
            print(column)
            print("One column") #Testing line