# # -*- coding: utf-8 -*-
import numpy as np

# We open the file and read the lines
f = open('input.txt', 'r')
lines = f.readlines()
# Dont forget to close the file
f.close()

# # We create a list of the elves calories, starting by one elf with 0 calories
# current_elf_calories = 0
# # We need to compute the maximum number of calories, we start with 0
# # these maximums are sorted
# max_value1 = 0
# max_value2 = 0
# max_value3 = 0

# # We iterate over the lines
# for l in lines:
#     # If the line is empty, we jump to the next elf
#     # we use the strip function to remove the \n character
#     l = l.strip()
#     print("Current elf:" + str(current_elf_calories))
#     if l == '':
#         # We check if the current elf has more calories than the maximum
#         if max_value1 <= current_elf_calories:
#             print("Old max1: " + str(max_value1))
#             max_value1 = current_elf_calories
#         elif max_value2 <= current_elf_calories:
#             print("Old max2: " + str(max_value2))
#             max_value2 = current_elf_calories
#         elif max_value3 <= current_elf_calories:
#             print("Old max3: " + str(max_value3))
#             max_value3 = current_elf_calories
#         # We add a new elf with 0 calories
#         current_elf_calories = 0
#     else:
#         # We sum the calories of the current line to the current elf
#         # We use the strip function to remove the \n character
#         current_elf_calories+=int(l)
    
# # Print the sum of the three maximum
# print(max_value1)
# print(max_value1+max_value2+max_value3)

# The solution above does not seems to work, we walk around!

# First we compute the calories
calories = [0]
for l in lines:
    l = l.strip()
    if l=='':
        calories.append(0)
    else:
        calories[-1]+=int(l)

# Sort the array
calories=np.array(calories)
calories = np.sort(calories)

# Print the last and the sum of the three last elements!
print(calories[-1])
print(calories[-1]+calories[-2]+calories[-3])