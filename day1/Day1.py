# count = 0
# dial = 50
# loop_counter = 0
# with open("input_data.txt", 'r') as f:
#   for line in f:
#     direction = line[0]
#     steps = int(line[1:])

#     larger_100, resten = (steps // 100, steps % 100) if steps > 99 else (0, steps)
#     count += larger_100

#     if direction == "R":
#         if (dial + resten) >= 100:
#             count += 1
#         dial = (dial + resten) % 100

#     else: 
#         if (dial - resten) < 0:
#             count += 1
#         dial = (dial - resten) % 100

#     if dial == 0:
#         count += 1

# print(count)


def hits_zero(dial: int, direction: str, steps: int) -> int:
    if direction == "R":
        first = (100 - dial) % 100
    else:  # "L"
        first = dial % 100

    if first == 0:
        first = 100  # you only hit 0 after 100 clicks if you're already at 0

    if steps < first:
        return 0
    return 1 + (steps - first) // 100


count = 0
dial = 50

with open("input_data.txt", "r") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        steps = int(line[1:])

        count += hits_zero(dial, direction, steps)

        if direction == "R":
            dial = (dial + steps) % 100
        else:
            dial = (dial - steps) % 100

print(count)
