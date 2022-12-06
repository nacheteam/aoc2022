import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()[0]

for i in range(4,len(data)):
    print(data[i-4:i])
    if len(set(data[i-4:i])) == 4:
        print(i)
        break

for i in range(14,len(data)):
    print(data[i-14:i])
    if len(set(data[i-14:i])) == 14:
        print(i)
        break