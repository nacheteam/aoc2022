import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()

cycle = 1
x = 1

signal = []

for line in data:
    if (cycle-20) % 40 == 0:
        signal.append(x*cycle)
    if "noop" in line:
        cycle += 1
    else:
        cycle += 1
        if (cycle-20) % 40 == 0:
            signal.append(x*cycle)
        cycle += 1
        x += int(line.split(" ")[1])

print(np.sum(signal))


# Part 2
x = 1
sprite = np.zeros(40)
sprite[x-1:x+2] = 1
cycle_crt = 0
screen = []
for line in data:
    if cycle_crt%40 in np.where(sprite == 1)[0]:
        screen.append("#")
    else:
        screen.append(".")
    if "noop" in line:
        cycle_crt += 1
    else:
        cycle_crt += 1
        if cycle_crt%40 in np.where(sprite == 1)[0]:
            screen.append("#")
        else:
            screen.append(".")
        cycle_crt += 1
        x += int(line.split(" ")[1])
        sprite = np.zeros(40)
        sprite[x-1:x+2] = 1

screen = np.array(screen).reshape(6,40)
for line in screen:
    print("".join(line))
