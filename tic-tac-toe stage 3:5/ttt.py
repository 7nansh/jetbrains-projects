# write your code here
symbols = input("Enter cells: ")

field = [
    [symbols[0], symbols[1], symbols[2]],
    [symbols[3], symbols[4], symbols[5]],
    [symbols[6], symbols[7], symbols[8]]
]

both_win = False
x_win = False
o_win = False

xs = [x for x in symbols if x == "X"]
os = [x for x in symbols if x == "O"]
blanks = [x for x in symbols if x == "_"]

win_states = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

xo_more = len(xs) - len(os) >= 2 or len(os) - len(xs) >= 2

print("---------")
for i in range(3):
    out = "| "
    for j in range(3):
        out += field[i][j] + " "
    out += "|"
    print(out)
print("---------")

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

# checking if both win
if x_win and o_win:
    both_win = True

if xo_more or both_win:
    # if
    print("Impossible")
elif x_win:
    print("X wins")
elif o_win:
    print("O wins")
elif len(blanks) != 0 and x_win is False and o_win is False:
    print("Game not finished")
else:
    print("Draw")
