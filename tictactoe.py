 board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

game_running = True
winner = None
current_player = 'X'

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def play_game():
    display_board()

    while game_running:

        handle_turn(current_player)

        game_status()

        flip_player()

    #game has ended
    if winner == 'X' or winner == 'O':
      print(winner + " won!")
    elif winner == None:
      print('Tie')

def handle_turn(player):

  print(player + "'s Turn.")
  position = input('Please, choose a number between 1 and 9: ')

  valid = False
  while not valid:

    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      position = input('Invalid Input. Please, choose a number between 1 and 9: ')

    position = int(position) - 1

    if board[position] == '-':
      valid = True
    else:
      position = input('This location has already been selected. Please choose another number between 1 and 9: ')

  board[position] = player
  display_board()

def game_status():
    check_win()
    check_tie()

def check_win():
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonal()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return

def check_rows():
  global game_running
  row_1 = board[0] == board[1] == board[2] != '-'
  row_2 = board[3] == board[4] == board[5] != '-'
  row_3 = board[6] == board[7] == board[8] != '-'

  if row_1 or row_2 or row_3:
    game_running = False

  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
  global game_running
  column_1 = board[0] == board[3] == board[6] != '-'
  column_2 = board[1] == board[4] == board[7] != '-'
  column_3 = board[2] == board[5] == board[8] != '-'

  if column_1 or column_2 or column_3:
    game_running = False

  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonal():
  global game_running
  diagonal_1 = board[0] == board[4] == board[8] != '-'
  diagonal_2 = board[2] == board[4] == board[6] != '-'

  if diagonal_1 or diagonal_2:
    game_running = False

  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return

def check_tie():
  global game_running
  if '-' not in board:
    game_running = False
  return

def flip_player():
  global current_player
  if current_player == 'X':
    current_player = 'O'
  elif current_player == 'O':
    current_player = 'X'
  return

play_game()
