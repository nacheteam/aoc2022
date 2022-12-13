import numpy as np

total_rounds = 20
monkeys = {}

with open("input.txt") as f:
    data = f.read().splitlines()

current_monkey = -1
for line in data:
    if not "Monkey" in line:
        # 0 will be the item list
        # 1 will be the operation multiplier
        # 2 will be the division test factor
        # 3 will be the monkey in the true scenario
        # 4 will be the monkey in the false scenario
        if "items" in line:
            item = line.split(":")[1].split(",")
            item = [int(i.strip()) for i in item]
            monkeys[current_monkey] = [item]
        elif "Operation" in line:
            operation, factor = None, None
            if "+" in line:
                operation = "+"
                factor = line.split("+")[1].strip()
            else:
                operation = "*"
                factor = line.split("*")[1].strip()
            multiplier = [operation, factor]
            monkeys[current_monkey].append(multiplier)
        elif "Test" in line:
            division_factor = int(line.split("by")[1].strip())
            monkeys[current_monkey].append(division_factor)
        elif "true" in line:
            monkey_true = int(line.split("monkey")[1].strip())
            monkeys[current_monkey].append(monkey_true)
        elif "false" in line:
            monkey_false = int(line.split("monkey")[1].strip())
            monkeys[current_monkey].append(monkey_false)
    if "Monkey" in line:
        monkey_id = int(line.split(" ")[1].split(":")[0])
        monkeys[monkey_id] = []
        current_monkey = monkey_id


business = [0 for i in range(len(monkeys))]
monkey_ids = list(monkeys.keys())
    
for i in range(total_rounds):
    print("Round: ", i, end="\r")
    for monkey_id in monkey_ids:
        monkey = monkeys[monkey_id]
        business[monkey_id] += len(monkey[0])
        for item_number,item in enumerate(monkey[0]):
            if monkey[1][0] == "+":
                new_value = int(item) + int(monkey[1][1]) if monkey[1][1] != "old" else int(item) + int(item)
            else:
                new_value = int(item) * int(monkey[1][1]) if monkey[1][1] != "old" else int(item) * int(item)
            new_value = int(new_value/3)
            if new_value % monkey[2] == 0:
                monkeys[monkey[3]][0].append(new_value)
            else:
                monkeys[monkey[4]][0].append(new_value)
        monkeys[monkey_id][0] = []

print("\n####################")
print("Result: ", np.prod(np.sort(business)[::-1][:2]))


# Part 2
total_rounds = 10000
monkeys = {}

with open("input.txt") as f:
    data = f.read().splitlines()

current_monkey = -1
for line in data:
    if not "Monkey" in line:
        # 0 will be the item list
        # 1 will be the operation multiplier
        # 2 will be the division test factor
        # 3 will be the monkey in the true scenario
        # 4 will be the monkey in the false scenario
        if "items" in line:
            item = line.split(":")[1].split(",")
            item = [int(i.strip()) for i in item]
            monkeys[current_monkey] = [item]
        elif "Operation" in line:
            operation, factor = None, None
            if "+" in line:
                operation = "+"
                factor = line.split("+")[1].strip()
            else:
                operation = "*"
                factor = line.split("*")[1].strip()
            multiplier = [operation, factor]
            monkeys[current_monkey].append(multiplier)
        elif "Test" in line:
            division_factor = int(line.split("by")[1].strip())
            monkeys[current_monkey].append(division_factor)
        elif "true" in line:
            monkey_true = int(line.split("monkey")[1].strip())
            monkeys[current_monkey].append(monkey_true)
        elif "false" in line:
            monkey_false = int(line.split("monkey")[1].strip())
            monkeys[current_monkey].append(monkey_false)
    if "Monkey" in line:
        monkey_id = int(line.split(" ")[1].split(":")[0])
        monkeys[monkey_id] = []
        current_monkey = monkey_id


business = [0 for i in range(len(monkeys))]
monkey_ids = list(monkeys.keys())
print("Number of monkeys: ", len(monkey_ids))
reduction_factor = 1
for monkey_id in monkey_ids:
    monkey = monkeys[monkey_id]
    reduction_factor*=monkey[2]
    
for i in range(total_rounds):
    print("Round: ", i, end="\r")
    for monkey_id in monkey_ids:
        monkey = monkeys[monkey_id]
        business[monkey_id] += len(monkey[0])
        for item_number,item in enumerate(monkey[0]):
            if monkey[1][0] == "+":
                new_value = int(item) + int(monkey[1][1]) if monkey[1][1] != "old" else int(item) + int(item)
            else:
                new_value = int(item) * int(monkey[1][1]) if monkey[1][1] != "old" else int(item) * int(item)
            new_value %= reduction_factor
            if new_value % monkey[2] == 0:
                monkeys[monkey[3]][0].append(new_value)
            else:
                monkeys[monkey[4]][0].append(new_value)
        monkeys[monkey_id][0] = []

print("\n####################")
print("Result: ", np.prod(np.sort(business)[::-1][:2].astype(np.int64)))
