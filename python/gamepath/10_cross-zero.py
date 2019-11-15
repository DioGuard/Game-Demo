# Game Cross-Zero | Игра Крестики-Нолики
# Глобальные переменные

X = "X"
O = "O"
EMPTY = " "
COUNT_SQUARES = 9
TIE = "Ничья"

def display_instruct():
    """Выводит на экран инструкцию для игрока"""
    print("""
    Добро пожаловать на невероятнейшее! грандиознейшее! сражение
    за титул лучшего игрока во вселенной в легендарной игре "Крестики нолики"!

    Правила игры просты:
        - тебе нужно собрать ряд из 3 одиноковых фишек по вертикали, горизонтали или же по диагонали
        раньше чем их соберёт твой гениальнейший противник, он же Его Высочество Компьютер.
        - выбор нужной позиции будет осуществляться с помощью ввода цифры из диапозона 0 - 8
        как показанно в нижестоящей таблице
        +---+---+---+
        | 0 | 1 | 2 |
        +---+---+---+
        | 3 | 4 | 5 |
        +---+---+---+
        | 6 | 7 | 8 |
        +---+---+---+
    Так начнётся же легендарное противостояние: моё железо vs твоей органики!
""")

def ask_yes_no(question):
    """Задаёт да-нет вопрос"""
    response = None
    while response not in ("n", "y", "н", "д"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Запрашивает ввод числа строгого диапазона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Определяет за кем первый ход"""
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? (д/н): ")
    if go_first in ("y", "д"):
        print("Тогда играй крестиками, хотя врятли тебе это поможет, хех.")
        human = X
        computer = O
    else:
        print("Как хочешь, но в таком случае я б не рассчитывал на лёгкую победу, или вообще на победу, хах.")
        computer = X
        human = O
    return human, computer

def new_board():
    """Создаёт новую игровую доску"""
    board = []
    for square in range(COUNT_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Выводит игровую доску на экране"""
    print("+---+---+---+")
    for square in range(COUNT_SQUARES):
        print("| " + board[square], end=" ")
        if(square + 1) % 3 == 0:
            print("|\n+---+---+---+")

def legal_moves(board):
    """Создаёт список доступных ходов"""
    moves = []
    for square in range(COUNT_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Определяет победителя в игре"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            return board[row[0]]
        if EMPTY not in board:
            return TIE
    return None

def human_moves(board):
    """Определяет ход игрока"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0 - 8):", 0, COUNT_SQUARES)
        if move not in legal:
            print("\nПоле занято или не сущетвует!\n")
        print("Ладно...")
    return move

def comp_moves(board, comp, human):
    """Определяет ход компьютера"""
    board = board[:]
    BEST_MOVE = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выбираю поле с номером:", end=" ")

    for move in legal_moves(board):
        board[move] = comp
        if winner(board) == comp:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVE:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Осуществляет переход хода"""
    if turn == X:
        return O
    else:
        return X

def congratulations(the_winner, human, comp):
    """Поздравляет победителя игры"""
    if the_winner == human:
        print("Три " + the_winner + " в ряд!")
        print("Чёрт! Возможно в этот раз органика и взяла вверх над механикой, но в следующий раз я не допущу подобного!")
    elif the_winner == comp:
        print("Три " + the_winner + " в ряд!")
        print("Ничего другого и не следовало ожидать. Никто не в силах изменить свою судьбу.\n"
              "Приходи вновь, если наберёшься силушек вновь противостоять мне.")
    else:
        print("Ничья")
        print("Не может быть. Похоже я недооценил твою угрозу, человечишка.")

def main():
    display_instruct()
    human, comp = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            board[human_moves(board)] = human
        else:
            board[comp_moves(board, comp, human)] = comp

        display_board(board)
        turn = next_turn(turn)

    congratulations(winner(board), human, comp)

# Оснавная часть
main()
print("Нажмите ENTER, чтобы выйти...")