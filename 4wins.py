timport numpy as np

def createboard():
  board = np.zeros((6,7),dtype = int)
  return board

def make_move(board, column, player):
  while column < 1 or column > 7 or board[0, column - 1] != 0:
    if column < 1 or column > 7:
      print("Choose another column, this one is non existent")
    elif board[0, column - 1] != 0:
      print("Choose another column, this one is too full")
    column = int(input("New column:"))

  # Find next free spot in column
  row = 5
  while board[row, column - 1] != 0:
    row -= 1

  # Mark the cell
  board[row, column - 1] = player


def check_win(board, player):

  # horizontal win
  for row in range(6):
    for col in range(4):
      if board[row, col] == player and board[row, col + 1] == player and board[row, col + 2] == player and board[row, col + 3] == player:
        return True

  # Vertikal win
  for row in range(3):
    for col in range(7):
      if board[row, col] == player and board[row + 1, col] == player and board[row + 2, col] == player and board[row + 3, col] == player:
        return True
      
  # Diagonal wins
  for row in range(3):
    for col in range(4):
      if board[row, col] == player and board[row + 1, col + 1] == player and board[row + 2, col + 2] == player and board[row + 3, col + 3] == player:
        return True
  for row in range(3):
    for col in range(3):
      if board[row, col + 3] == player and board[row + 1, col + 2] == player and board[row + 2, col + 1] == player and board[row + 3, col] == player:
        return True

  return False


def print_board(board):
  'better looking game board
  print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
  for row in board:
    for cell in row:
      if cell == 0:
        print("|   ", end="")
      elif cell == 1:
        print("| X ", end="")
      else:
        print("| O ", end="")
    print("|")


def play_game():
  board = createboard()
  current_player = 1
  while True:
    print_board(board)

    # Get where the player will put his coin/mark/howeveryoucallit
    column = int(input("Spieler {}: Choose a column (1-7): ".format(current_player)))
    make_move(board, column, current_player)

    # see if the game ends
    if check_win(board, current_player):
      print_board(board)
      print("")
      print("Spieler {} wins!".format(current_player))
      print("")
      print(play_game())
    if np.all(board[0, :] != 0) and not check_win(board, 1) and not check_win(board, 2):
      print_board(board)      
      print("")
      print("Tie! The board is full.")
      print("")
      print(play_game())

    # switch to next player
    if current_player == 1:
      current_player += 1
    else: 
      current_player -= 1

print(play_game())
