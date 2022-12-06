import numpy as np

# Define a function to compute the intersection between a list of strings
def compute_intersection(list_of_strings):
    # Initialize the intersection with the first string
    intersection = set(list_of_strings[0])
    # Loop over the remaining strings
    for string in list_of_strings[1:]:
        # Compute the intersection with the current string
        intersection = intersection.intersection(set(string))
    # Return the intersection
    return list(intersection)

with open('input.txt') as f:
    lines = f.read().splitlines()

base_priority_lowercase = ord("a")-1    # 96
base_priority_uppercase = ord("A")-1    # 64
total_priority = 0
for l in lines:
    slice1 = l[:int(len(l)/2)]
    slice2 = l[int(len(l)/2):]
    common_item = ''.join(set(slice1).intersection(slice2))
    if common_item.islower():
        total_priority += ord(common_item) - base_priority_lowercase
    else:
        total_priority += ord(common_item) - base_priority_uppercase + 26

print(total_priority)

base_priority_lowercase = ord("a")-1    # 96
base_priority_uppercase = ord("A")-1    # 64
total_priority = 0
for i in range(0,len(lines)-2,3):
    group = lines[i:i+3]
    common_item = compute_intersection(group)[0]
    if common_item.islower():
        total_priority += ord(common_item) - base_priority_lowercase
    else:
        total_priority += ord(common_item) - base_priority_uppercase + 26

print(total_priority)