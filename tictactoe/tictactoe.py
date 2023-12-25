"""Tictactoe"""


def print_board(cells):
    """
    Print tictactoe board

    Parameters:
    cells (list): show current state of the board

    Returns:
        ...
    """
    print("---------")

    for i in range(0, 9, 3):
        row = "| " + " ".join(cells[i:i + 3]) + " |"
        print(row)

    print("---------")


def analyze_game():
    """
    Analise current state of game

    Parameters:
    cells (list): show current state of the board

    Returns:
         str: result of the game
    """
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if all(cells[i] == 'X' for i in combo):
            return "X wins"
        elif all(cells[i] == 'O' for i in combo):
            return "O wins"

    if '_' not in cells:
        return "Draw"


def move(player):
    """
    Allow player to make move

    Parameters:
    player (str): current player

    Returns:
        ...
    """
    while True:
        try:
            coordinates = input("Enter the coordinates: ").split()
            row, col = int(coordinates[0]) - 1, int(coordinates[1]) - 1

            if 0 <= row <= 2 and 0 <= col <= 2:
                index = row * 3 + col

                if cells[index] == '_':
                    cells[index] = player
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")


cells = ['_'] * 9
print_board(cells)

while True:
    move('X')
    print_board(cells)
    result = analyze_game()
    if result:
        print(result)
        break

    move('O')
    print_board(cells)
    result = analyze_game()
    if result:
        print(result)
        break
