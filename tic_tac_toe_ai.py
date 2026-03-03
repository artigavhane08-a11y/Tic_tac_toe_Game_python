board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def best_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return

# 🔥 GAME LOOP (KHUP IMPORTANT — left side la)
while True:
    print_board()

    user_move = int(input("Enter position (0-8): "))

    if board[user_move] == " ":
        board[user_move] = "X"
    else:
        print("Invalid Move!")
        continue

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if " " not in board:
        print("Draw!")
        break

    best_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break
