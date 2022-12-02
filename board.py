# Import the scikit-learn module for machine learning
import sklearn
import numpy as np
# Load the trained model from a file
model = np.load("tic-tac-toe-model.data")

# Function to check if a player has won the game


def player_has_won(board, player):
    # Check for horizontal wins
    for row in board:
        if row == [player, player, player]:
            return True

    # Check for vertical wins
    for i in range(3):
        if (board[0][i] == player and
            board[1][i] == player and
                board[2][i] == player):
            return True

    # Check for diagonal wins
    if (board[0][0] == player and
        board[1][1] == player and
            board[2][2] == player):
        return True

    if (board[0][2] == player and
        board[1][1] == player and
            board[2][0] == player):
        return True

    # If no wins were found, return False
    return False

# Function to check if the game is a draw


def game_is_a_draw(board):
    # Check for empty spaces on the board
    for row in board:
        if " " in row:
            return False

    # If no empty spaces were found, return True
    return True


# Create an empty tic-tac-toe board
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# Print the board to the console
for row in board:
    print(" ".join(row))

# Create a variable to track


# Create a loop to run until the game is over
while True:
    # Check if it is the AI's turn
    if player == "O":
        # Use the trained model to predict the best move
        prediction = model.predict(board)

        # Update the board to occupy the predicted space with the AI's symbol
        board[prediction[0]][prediction[1]] = player
    else:
        # Prompt the player to enter the coordinates of the space they want to occupy
        row = int(input("Player " + player +
                  ", enter the row of the space you want to occupy: "))
        column = int(input("Player " + player +
                     ", enter the column of the space you want to occupy: "))

        # Update the board to occupy the specified space with the player's symbol
        board[row][column] = player

    # Check if the player has won or if the game is a draw
    # If the game is over, break out of the loop
    if player_has_won(board, player) or game_is_a_draw(board):
        break

    # Switch to the other player's turn
    player = "X" if player == "O" else "O"

    # Print the board to the console
    for row in board:
        print(" ".join(row))


# Create a loop to run until the game is over
while True:
    # Check if it is the AI's turn
    if player == "O":
        # Use the trained model to predict the best move
        prediction = model.predict(board)

        # Update the board to occupy the predicted space with the AI's symbol
        board[prediction[0]][prediction[1]] = player
    else:
        # Prompt the player to enter the coordinates of the space they want to occupy
        row = int(input("Player " + player +
                  ", enter the row of the space you want to occupy: "))
        column = int(input("Player " + player +
                     ", enter the column of the space you want to occupy: "))

        # Update the board to occupy the specified space with the player's symbol
        board[row][column] = player

    # Check if the player has won or if the game is a draw
    # If the game is over, break out of the loop
    if player_has_won(board, player) or game_is_a_draw(board):
        break

    # Switch to the other player's turn
    player = "X" if player == "O" else "O"

    # Print the board to the console
    for row in board:
        print(" ".join(row))

        # Function to get the outcome of the game


def get_outcome(board, player):
    # Check if the current player has won
    if player_has_won(board, player):
        return "win"

    # Check if the game is a draw
    if game_is_a_draw(board):
        return "draw"

    # If the game is not a win or a draw, the other player has won
    return "loss"


# Determine the outcome of the game
outcome = get_outcome(board, player)

# Print the outcome of the game
if outcome == "win":
    print("Player " + player + " wins!")
elif outcome == "draw":
    print("The game is a draw!")
else:
    print("Player " + other_player + " wins!")
