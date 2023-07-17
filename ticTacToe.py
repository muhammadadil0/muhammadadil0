board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

def print_board(board):
    for row in board:
        for slot in row:
            print(slot, end=" ")
        print()


count = 1
while True:
    print_board(board)
    playerRow = int(input("Player 1: Enter the row (0-2): "))
    playerCol = int(input("Player 1: Enter the column (0-2): "))
    board[playerRow][playerCol] = 'x'
    print_board(board)

    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
        print("Player 1 wins the game!")
        break

    elif board[1][0] == board[1][1] == board[1][2] == 'x':
        print("Player 1 wins the game!")
        break

    elif board[2][0] == board[2][1] == board[2][2] == 'x':
        print("Player 1 wins the game!")
        break

    elif board[0][0] == board[1][0] == board[2][0] == 'x':
        print("Player 1 wins the game!")
        break

    elif board[0][1] == board[1][1] == board[2][1] == 'x':
        print("Player 1 wins the game!")
        break

    elif board[0][2] == board[1][2] == board[2][2] == 'x':
        print("Player 1 wins the game!")
        break

    elif board[0][0] == board[1][1] == board[2][2] == 'x':
        print("Player 1 wins the game!")
        break

    elif board[0][2] == board[1][1] == board[2][0] == 'x':
        print("Player 1 wins the game!")
        break

    player2Row = int(input("Player 2: Enter the row (0-2): "))
    player2Col = int(input("Player 2: Enter the column (0-2): "))
    board[player2Row][player2Col] = 'o'

    count = count + 1

    if board[0][0] == board[0][1] == board[0][2] == 'o':
        print("Player 2 wins the game!")
        break

    elif board[1][0] == board[1][1] == board[1][2] == 'o':
        print("Player 2 wins the game!")
        break

    elif board[2][0] == board[2][1] == board[2][2] == 'o':
        print("Player 2 wins the game!")
        break

    elif board[0][0] == board[1][0] == board[2][0] == 'o':
        print("Player 2 wins the game!")
        break

    elif board[0][1] == board[1][1] == board[2][1] == 'o':
        print("Player 2 wins the game!")
        break

    elif board[0][2] == board[1][2] == board[2][2] == 'o':
        print("Player 2 wins the game!")
        break

    elif board[0][0] == board[1][1] == board[2][2] == 'o':
        print("Player 2 wins the game!")
        break

    elif board[0][2] == board[1][1] == board[2][0] == 'o':
        print("Player 2 wins the game!")
        break
# print_board(board)




