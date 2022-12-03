input_data = []
with open("day3_input.txt") as f:
    input_data = [item.replace("\n", "") for item in f]

points = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0
for rucksack in input_data:
    item_len = int(len(rucksack) / 2)
    first_item = rucksack[item_len:]
    sec_item = rucksack[:item_len]
    duplicate = [n for n in first_item if sec_item.count(n) >= 1][0]
    if duplicate:
        result += points.index(duplicate)

print(result)
