with open("day8_input.txt") as f:
    input_data = [item.replace("\n", "") for item in f]

input_data = list(map(lambda row: list(map(int, [*row])), input_data))
transposed = list(map(list, zip(*input_data)))
count = 0
max_score = 0


for y, row in enumerate(input_data):
    for x, tree in enumerate(row):
        score = 1

        if x == 0 or y == 0 or x == len(row) - 1 or y == len(input_data) - 1:
            count += 1
            continue

        visible_x = max(row[:x]) < tree or max(row[x + 1 :]) < tree
        visible_y = max(transposed[x][:y]) < tree or max(transposed[x][y + 1 :]) < tree
        if visible_x or visible_y:
            count += 1

        directions = [
            row[x + 1 :],
            list(reversed(row[:x])),
            transposed[x][y + 1 :],
            list(reversed(transposed[x][:y])),
        ]

        for direction in directions:
            _score = 0
            for i in direction or []:
                _score += 1
                if i >= tree:
                    break
            score *= _score

        if score > max_score:
            max_score = score


print(count)
print(max_score)
