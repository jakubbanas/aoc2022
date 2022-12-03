with open("day1_input.txt") as f:
    input_data = [item.replace("\n", "") for item in f]

current = 0
sums = []
for item in input_data:
    if item == "":
        sums.append(current)
        current = 0
        continue
    current += int(item)

sums.sort(reverse=True)

print(sums[0])
print(sum(sums[:3]))
