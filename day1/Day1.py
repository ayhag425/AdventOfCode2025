
data = []
count = 0
dial = 50
loop_counter = 0
with open("input_data.txt", 'r') as f:
  for line in f:
    direction = line[0]
    steps = int(line[1:])

    if direction == "R":
        dial = (dial + steps) % 100
    else: 
        dial = (dial - steps) % 100

    if dial == 0:
        count += 1

print(count)




