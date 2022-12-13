import numpy as np
from queue import PriorityQueue

def estimate_cost(pos, final_pos):
    return np.abs(pos[0] - final_pos[0]) + np.abs(pos[1] - final_pos[1])

def get_neighbours(terrain, cost_map, pos, cost):
    neighbours = []
    if pos[0] > 0:
        if terrain[pos[0] - 1, pos[1]] - terrain[pos[0], pos[1]]<=1:
            new_pos = (pos[0] - 1, pos[1])
            new_cost = cost-cost_map[pos[0],pos[1]]+1+cost_map[new_pos[0],new_pos[1]]
            neighbours.append((new_cost,new_pos))
    if pos[0] < terrain.shape[0] - 1:
        if terrain[pos[0] + 1, pos[1]] - terrain[pos[0], pos[1]]<=1:
            new_pos = (pos[0] + 1, pos[1])
            new_cost = cost-cost_map[pos[0],pos[1]]+1+cost_map[new_pos[0],new_pos[1]]
            neighbours.append((new_cost,new_pos))
    if pos[1] > 0:
        if terrain[pos[0], pos[1] - 1] - terrain[pos[0], pos[1]]<=1:
            new_pos = (pos[0], pos[1] - 1)
            new_cost = cost-cost_map[pos[0],pos[1]]+1+cost_map[new_pos[0],new_pos[1]]
            neighbours.append((new_cost,new_pos))
    if pos[1] < terrain.shape[1] - 1:
        if terrain[pos[0], pos[1] + 1] - terrain[pos[0], pos[1]]<=1:
            new_pos = (pos[0], pos[1] + 1)
            new_cost = cost-cost_map[pos[0],pos[1]]+1+cost_map[new_pos[0],new_pos[1]]
            neighbours.append((new_cost,new_pos))
    return neighbours

def find_path(terrain, cost_map, start_pos):
    # Define the open and closed lists
    open_list = PriorityQueue()
    closed_list = set()
    # iterate from the start position
    open_list.put((0+cost_map[start_pos[0],start_pos[1]], start_pos))
    while not open_list.empty():
        # get the current position
        current_cost, current_pos = open_list.get()
        #print("Abiertos: ",len(open_list.queue),", Cerrados: ", len(closed_list), ", Tamaño total: ", terrain.shape[0]*terrain.shape[1],
        #", Longitud actual: ", current_cost, ", Longitud estimada: ", cost_map[start_pos[0],start_pos[1]],
        #", %visitados: ", 100*len(closed_list)/(terrain.shape[0]*terrain.shape[1]), end="\r")
        # if we have reached the final position, return the path
        if cost_map[current_pos[0],current_pos[1]] == 0:
            return current_cost
        # if we have not reached the final position, add the current position to the closed list
        closed_list.add(current_pos)
        # get the neighbours of the current position
        neighbours = get_neighbours(terrain, cost_map, current_pos, current_cost)
        # iterate through the neighbours
        for neighbour in neighbours:
            # if the neighbour is in the closed list, skip it
            if neighbour[1] in closed_list:
                continue
            # if the neighbour is not in the open list, add it
            if neighbour not in open_list.queue:
                open_list.put(neighbour)
    return np.inf

with open("input.txt") as f:
    data = f.read().splitlines()

terrain = np.zeros((len(data), len(data[0])))
cost_map = np.zeros((len(data), len(data[0])))
start_pos = (0, 0)
final_pos = (0, 0)
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "S":
            terrain[i, j] = 0
            start_pos = (i, j)
        elif char == "E":
            terrain[i, j] = ord("z") - ord("a")
            final_pos = (i, j)
        else:
            terrain[i, j] = ord(char) - ord("a")

for i in range(terrain.shape[0]):
    for j in range(terrain.shape[1]):
        cost_map[i, j] = estimate_cost((i, j), final_pos)

path_length = find_path(terrain, cost_map, start_pos)
print("\nPath length: ", path_length)

lowest_positions = []
for i in range(terrain.shape[0]):
    for j in range(terrain.shape[1]):
        if terrain[i, j] == terrain.min():
            lowest_positions.append((i, j))

min_path_length = np.inf
cont = 0
for lowest_pos in lowest_positions:
    cont += 1
    print("Lowest position: ", cont, "/", len(lowest_positions), end="\r")
    path_length = find_path(terrain, cost_map, lowest_pos)
    if path_length < min_path_length:
        min_path_length = path_length

print("\nMin path length: ", min_path_length)