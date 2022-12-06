import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()

stack_list = [[] for _ in range(9)]
read_stacks = True

for d in data:
    if len(d)==0:
        read_stacks=False
        for i in range(len(stack_list)):
            stack_list[i] = stack_list[i][::-1][1:]
    else:
        if read_stacks:   
            st = 0 
            for i in range(1,len(d),4):
                if d[i] != " ":
                    stack_list[st].append(d[i])
                st+=1
        else:
            num_elem = int(d.split(" ")[1])
            orig = int(d.split(" ")[3])-1
            dest = int(d.split(" ")[5])-1
            stack_list[dest] = stack_list[dest] + stack_list[orig][-num_elem:][::-1]
            stack_list[orig] = stack_list[orig][:-num_elem]

cad = ""
for st in stack_list:
    cad += st[-1]
print(cad)


# Part 2
with open("input.txt", "r") as f:
    data = f.read().splitlines()

stack_list = [[] for _ in range(9)]
read_stacks = True

for d in data:
    if len(d)==0:
        read_stacks=False
        for i in range(len(stack_list)):
            stack_list[i] = stack_list[i][::-1][1:]
    else:
        if read_stacks:   
            st = 0 
            for i in range(1,len(d),4):
                if d[i] != " ":
                    stack_list[st].append(d[i])
                st+=1
        else:
            num_elem = int(d.split(" ")[1])
            orig = int(d.split(" ")[3])-1
            dest = int(d.split(" ")[5])-1
            stack_list[dest] = stack_list[dest] + stack_list[orig][-num_elem:]
            stack_list[orig] = stack_list[orig][:-num_elem]

cad = ""
for st in stack_list:
    cad += st[-1]
print(cad)