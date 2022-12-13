import numpy as np
from scipy.spatial.distance import cityblock

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

head = [0,0]
tail = [0,0]
coordinates_visited_tail = [[0,0]]
for line in data:
    direction, distance = line.split(" ")[0], int(line.split(" ")[1])
    increment_horizontal = 0 if direction == "U" or direction == "D" else 1 if direction == "R" else -1
    increment_vertical = 0 if direction == "L" or direction == "R" else 1 if direction == "D" else -1
    for i in range(distance):
        head = [head[0] + increment_horizontal, head[1] + increment_vertical]
        if cityblock(head, tail) > 1:
            if np.abs(head[0] - tail[0]) == cityblock(head, tail):
                tail[0] += increment_horizontal
            elif np.abs(head[1] - tail[1]) == cityblock(head, tail):
                tail[1] += increment_vertical
            else:
                if cityblock(head,tail)>2:
                    if direction == "U" or direction == "D":
                        tail[1] += increment_vertical
                        tail[0] = head[0]
                    else:
                        tail[0] += increment_horizontal
                        tail[1] = head[1]
        if tail not in coordinates_visited_tail:
            coordinates_visited_tail.append(tail.copy())

print(len(coordinates_visited_tail))

def twoknots(tail,head,direction,dont_move_head=False):
    increment_horizontal = 0 if direction == "U" or direction == "D" else 1 if direction == "R" else -1
    increment_vertical = 0 if direction == "L" or direction == "R" else 1 if direction == "D" else -1
    new_head = head.copy()
    new_head = [new_head[0] + increment_horizontal, new_head[1] + increment_vertical] if not dont_move_head else new_head
    new_tail = tail.copy()
    
    dist_x, dist_y = np.abs(new_head[0] - new_tail[0]), np.abs(new_head[1] - new_tail[1])
    if (np.abs(dist_x)>=2) and (np.abs(dist_y)>=2):
        new_tail = [new_head[0]-1 if new_tail[0]<new_head[0] else new_head[0]+1, new_head[1]-1 if new_tail[1]<new_head[1] else new_head[1]+1]
    elif np.abs(dist_x)>=2:
        new_tail = [new_head[0]-1 if new_tail[0]<new_head[0] else new_head[0]+1, new_tail[1]]
    elif np.abs(dist_y)>=2:
        new_tail = [new_tail[0], new_head[1]-1 if new_tail[1]<new_head[1] else new_head[1]+1]
    return new_tail, new_head

rope = [[0,0] for _ in range(9)]
coordinates_visited_tail = [[0,0]]
for line in data:
    direction, distance = line.split(" ")[0], int(line.split(" ")[1])
    for i in range(distance):
        for j in range(len(rope)-1):
            rope[j+1], rope[j] = twoknots(rope[j+1],rope[j],direction) if j==0 else twoknots(rope[j+1],rope[j],direction,True)
        if rope[-1] not in coordinates_visited_tail:
            coordinates_visited_tail.append(rope[-1].copy())

print(len(coordinates_visited_tail))