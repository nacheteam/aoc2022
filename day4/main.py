import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()

fully_contained = 0
for i in range(len(data)):
    pair1 = (int(data[i].split(",")[0].split("-")[0]), int(data[i].split(",")[0].split("-")[1]))
    pair2 = (int(data[i].split(",")[1].split("-")[0]), int(data[i].split(",")[1].split("-")[1]))
    # Check if pair1 is fully contained in pair2
    if pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
        fully_contained += 1
    # Check if pair2 is fully contained in pair1
    elif pair2[0] >= pair1[0] and pair2[1] <= pair1[1]:
        fully_contained += 1

print(fully_contained)

overlaped = 0
for i in range(len(data)):
    pair1 = (int(data[i].split(",")[0].split("-")[0]), int(data[i].split(",")[0].split("-")[1]))
    pair2 = (int(data[i].split(",")[1].split("-")[0]), int(data[i].split(",")[1].split("-")[1]))
    # Check if pair1 is overlaped with pair2
    if pair1[0] >= pair2[0] and pair1[0] <= pair2[1]:
        overlaped += 1
    # Check if pair2 is overlaped with pair1
    elif pair2[0] >= pair1[0] and pair2[0] <= pair1[1]:
        overlaped += 1
        
print(overlaped)