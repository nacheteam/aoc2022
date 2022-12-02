import numpy as np

# First part

with open('input.txt') as f:
    data = f.read().splitlines()

figure_score = {"A": 1, "B": 2, "C": 3}
figure_translation = {"X": "A", "Y": "B", "Z": "C"}

total_score = 0
for d in data:
    d = d.split()
    p1, p2 = d[0], d[1]
    total_score+=figure_score[figure_translation[p2]]
    if figure_translation[p2]==p1:
        total_score+=3
    elif p2=="X" and p1=="C":
        total_score+=6
    elif p2=="Y" and p1=="A":
        total_score+=6
    elif p2=="Z" and p1=="B":
        total_score+=6

print(total_score)

# Second part

winning_schema = {"X": 0, "Y": 3, "Z": 6}

total_score = 0
for d in data:
    d = d.split()
    p1, p2 = d[0], d[1]
    total_score+=winning_schema[p2]
    if p2=="Y":
        total_score+=figure_score[p1]
    elif p2=="X":
        if p1=="A":
            total_score+=figure_score["C"]
        elif p1=="B":
            total_score+=figure_score["A"]
        elif p1=="C":
            total_score+=figure_score["B"]
    elif p2=="Z":
        if p1=="A":
            total_score+=figure_score["B"]
        elif p1=="B":
            total_score+=figure_score["C"]
        elif p1=="C":
            total_score+=figure_score["A"]

print(total_score)