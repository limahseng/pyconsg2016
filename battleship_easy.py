from random import randint  # randint generates a random integer in the range provided

def print_board(board): 
    for row in board:
        print (" ".join(row)) # print board row by row

def random_row(board):
    return randint(0, len(board) - 1) # generate random number for board row index

def random_col(board):
    return randint(0, len(board[0]) - 1) # generate random number for board column index

# main
board = [] # initialize empty board

for x in range(3):
    board.append(["O"] * 3) # insert 3 rows of ["O","O","O"] into the board 

print("Let's play Battleship!")
print_board(board) 
ship_row = random_row(board) # place the ship at row
ship_col = random_col(board) # place the ship at column

turn = 1
while turn < 4:
    print("Turn", turn)
    guess_row = int(input("Guess Row: ")) - 1 # convert input row to integer board index
    guess_col = int(input("Guess Col: ")) - 1 # convert input column to integer board index
    # check hit
    if guess_row == ship_row and guess_col == ship_col: # if user hit the ship
        print ("Congratulations! You sunk the battleship!")
        break # exit loop
    else:
        if (guess_row < 0 or guess_row > 2) or (guess_col < 0 or guess_col > 2): # out of range
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"): # spot has already been hit
            print("You guessed that one already.")
        else: # the player hits an empty spot
            print("You missed the battleship!")
            board[guess_row][guess_col] = "X" 
            turn = turn + 1
            print_board(board)
        if turn == 4: # after 3 tries (turn starts from 1)
            print("Game Over")
            print("The Battleship is in row", ship_row + 1, ", col", ship_col + 1)
