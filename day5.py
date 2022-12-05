import copy

with open("day5_input.txt") as f:
    input_data = [item.replace("\n", "") for item in f]

"""
[V]     [B]                     [F]
[N] [Q] [W]                 [R] [B]
[F] [D] [S]     [B]         [L] [P]
[S] [J] [C]     [F] [C]     [D] [G]
[M] [M] [H] [L] [P] [N]     [P] [V]
[P] [L] [D] [C] [T] [Q] [R] [S] [J]
[H] [R] [Q] [S] [V] [R] [V] [Z] [S]
[J] [S] [N] [R] [M] [T] [G] [C] [D]
 1   2   3   4   5   6   7   8   9 
"""

state = [
    [],
    ["V", "N", "F", "S", "M", "P", "H", "I"],
    ["S", "R", "L", "M", "J", "D", "Q"],
    ["N", "Q", "D", "H", "C", "S", "W", "B"],
    ["R", "S", "C", "L"],
    ["M", "V", "T", "P", "F", "B"],
    ["T", "R", "Q", "N", "C"],
    ["G", "V", "R"],
    ["C", "Z", "S", "P", "D", "L", "R"],
    ["D", "S", "J", "V", "G", "P", "B", "F"],
]

state2 = copy.deepcopy(state)

# input_crates = input_data[:10]


for item in input_data[10:]:
    _, move, _, from_, _, to = item.split(" ")
    move = int(move)
    from_ = int(from_)
    to = int(to)

    for i in range(move):
        removed = state[from_].pop()
        state[to].append(removed)

    removed = state2[from_][-move:]
    state2[from_] = state2[from_][:-move]
    state2[to] += removed


format_output = lambda state: "".join([i[-1] for i in state if len(i) > 0])
print(format_output(state) == "SBPQRSCDF")  # SBPQRSCDF
print(format_output(state2) == "RGLVRCQSB")  # RGLVRCQSB
