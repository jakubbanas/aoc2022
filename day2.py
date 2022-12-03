with open("day2_input.txt") as f:
    input_data = [item.replace("\n", "") for item in f]

points_map = {"A": 1, "B": 2, "C": 3}
item_map = {"X": "A", "Y": "B", "Z": "C"}


def calculate_points(a, b) -> int:
    if a == b:
        return 3
    difference = points_map[b] - points_map[a]

    if difference == -2 or difference == 1:
        return 6

    return 0


def guess_move(a, b) -> str:
    map = [0, "A", "B", "C"]
    step = points_map[a]
    if b == "A":
        return map[step - 1 if step > 1 else step + 2]
    if b == "C":
        return map[step - 2 if step > 2 else step + 1]

    return map[step]


total_points = 0
sec_points = 0
for item in input_data:
    a, b = item.split(" ")
    b = item_map[b]
    total_points += calculate_points(a, b) + points_map[b]

    b = guess_move(a, b)
    sec_points += calculate_points(a, b) + points_map[b]

print(total_points)
print(sec_points)
