with open("day6_input.txt") as f:
    input_data = [item.replace("\n", "") for item in f][0]

frame = ""
result = 0
for index, item in enumerate(input_data[2:]):
    frame = input_data[index - 4 : index]
    is_distinct = len(set(frame)) != len(frame)
    if frame and not is_distinct:
        break
    result += 1
print(result)

result = 0
for index, item in enumerate(input_data[2:]):
    frame = input_data[index - 14 : index]
    is_distinct = len(set(frame)) != len(frame)
    if frame and not is_distinct:
        break
    result += 1
print(result)
