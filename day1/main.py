# # -*- coding: utf-8 -*-
import numpy as np
with open("input.txt") as f:
    c = np.array([int(l) if l else -1 for l in f.read().splitlines()])

e=np.split(c,np.where(c==-1)[0]+1)
e=np.sort(np.array([np.sum(e[i]) for i in range(len(e))]))

print(str(e[-1])+","+str(np.sum(e[-3:-1])))