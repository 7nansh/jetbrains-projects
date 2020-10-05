# write your code here
symbols = "_________"

field = [
    [symbols[0], symbols[1], symbols[2]],
    [symbols[3], symbols[4], symbols[5]],
    [symbols[6], symbols[7], symbols[8]]
]


win_states = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]


def print_field():
    print("---------")
    for i in range(3):
        out = "| "
        for j in range(3):
            out += field[i][j] + " "
        out += "|"
        print(out)
    print("---------")


print_field()


def n_to_p(n):
    if n < 0:
        return n * -1
    return n


def coordinates_to_list(x, y):
    return n_to_p(x-1), n_to_p(y-3)


def is_not_num(text):
    if text.split()[0] in "0123456789" and text.split()[1] in "0123456789":
        return False
    return True


current_player = "X"


while True:
    both_win = False
    x_win = False
    o_win = False

    xs = [x for x in symbols if x == "X"]
    os = [x for x in symbols if x == "O"]
    blanks = [x for x in symbols if x == "_"]

    xo_more = len(xs) - len(os) >= 2 or len(os) - len(xs) >= 2

    if x_win and o_win:
        both_win = True

    for win_state in win_states:
        if symbols[win_state[0]] == "X" and symbols[win_state[1]] == "X" and \
                symbols[win_state[2]] == "X":
            x_win = True
            break
    for win_state in win_states:
        if symbols[win_state[0]] == "O" and symbols[win_state[1]] == "O" and \
                symbols[win_state[2]] == "O":
            o_win = True
            break
    if xo_more or both_win:
        print("Impossible")
    elif x_win:
        print("X wins")
        break
    elif o_win:
        print("O wins")
        break
    elif len(blanks) != 0 and x_win is False and o_win is False:
        pass
    else:
        print("Draw")
        break
    next_move = input("Enter the coordinates:")
    nm = next_move.split()
    nm1 = "x"
    nm2 = "y"
    co = [nm1, nm2]
    if len(nm) > 1:
        nm1 = nm[0]
        nm2 = nm[1]
        if not is_not_num(next_move):
            nm1 = int(nm[0])
            nm2 = int(nm[1])
            co = coordinates_to_list(nm1, nm2)

    if is_not_num(next_move):
        print("You should enter numbers!")
    elif (nm1 < 1 or nm1 > 3) or (nm2 < 1 or nm2 > 3):
        print("Coordinates should be from 1 to 3!")
    elif field[co[1]][co[0]] == "X" or field[co[1]][co[0]] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        field[co[1]][co[0]] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        print_field()
        symbols = "".join(["".join(x) for x in field])
