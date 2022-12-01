# -*- coding: utf-8 -*-

# We open the file and read the lines
f = open('input.txt', 'r')
lines = f.readlines()
# Dont forget to close the file
f.close()

# We create a list of the elves calories, starting by one elf with 0 calories
currennt_elf_calories = 0
# We need to compute the maximum number of calories, we start with 0
max_value = 0

# We iterate over the lines
for l in lines:
    # If the line is empty, we jump to the next elf
    # we use the strip function to remove the \n character
    if l.strip() == '':
        # We check if the current elf has more calories than the maximum
        if max_value<currennt_elf_calories:
            max_value = currennt_elf_calories
        # We add a new elf with 0 calories
        currennt_elf_calories = 0
    else:
        # We sum the calories of the current line to the current elf
        # We use the strip function to remove the \n character
        currennt_elf_calories+=int(l.strip())
    
# Print the maximum number of calories
print(max_value)