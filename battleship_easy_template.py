# randint generates a random integer in the range provided

# function to print board row by row

# function to generate random number for board row index

# function to generate random number for board column index
    
    
# main
# initialize empty board

# insert 3 rows of ["O","O","O"] into the board

# show intro message

# show board

# place the ship at row

# place the ship at column

# create integer variable turn and initialize to 1

# loop if within 3 tries
    # show try number
    # convert input row to integer board index
    # convert input column to integer board index
    # check hit
    # if user hit the ship
        # show congratulatory message
        # exit loop
    # else
        # if out of range
            # show error message
        # if spot has already been hit
            # show already guessed message
        # if player hits empty spot
            # show empty hit message
            # mark spot as guessed with 'X' 
            # increment turn
            # show updated board
        # if after 3 tries
            # show game over message
            # reveal hidden ship location
