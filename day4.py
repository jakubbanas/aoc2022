with open("day4_input.txt") as f:
    input_data = [item.replace("\n", "") for item in f]

result, result2 = 0, 0
for item in input_data:
    a1, a2, b1, b2 = [int(i) for i in item.replace(",", "-").split("-")]
    result += (a1 <= b1 and b2 <= a2) or (b1 <= a1 and a2 <= b2)
    result2 += a2 >= b1 and a1 <= b2

print(result)
print(result2)
