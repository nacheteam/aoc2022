import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()

directories = {}
current_path = []
for line in data:
    split_line = line.split(" ")
    if split_line[1] == "cd":
        if split_line[2] == "..":
            current_path = current_path[:-1]
        else:
            current_path.append(split_line[2])
    elif split_line[1] == "ls":
        continue
    elif split_line[0] == "dir":
        continue   
    else:
        for i in range(1,len(current_path)+1):
            if "/".join(current_path[:i]) not in directories:
                directories["/".join(current_path[:i])] = 0
            directories["/".join(current_path[:i])] += int(split_line[0])


total_size = 0
for key, value in directories.items():
    if value < 100000:
        total_size += value
print(total_size)

free_space = 70000000 - directories["/"]
installation_needed = 30000000 - free_space
min_value = np.inf
for key, value in directories.items():
    if value>installation_needed:
        min_value = min(min_value, value)
print(min_value)