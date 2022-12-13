import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()

tree_matrix = np.zeros((len(data), len(data[0]))).astype(int)
for i in range(len(data)):
    for j in range(len(data[i])):
        tree_matrix[i,j] = data[i][j]

visible_trees = tree_matrix.shape[0]*2 + tree_matrix.shape[1]*2 - 4
for i in range(1,tree_matrix.shape[0]-1):
    for j in range(1,tree_matrix.shape[1]-1):
        max1 = np.amax(tree_matrix[0:i,j])
        max2 = np.amax(tree_matrix[i,0:j])
        max3 = np.amax(tree_matrix[i,j+1:])
        max4 = np.amax(tree_matrix[i+1:,j])
        min_height = min([max1, max2, max3, max4])
        if tree_matrix[i,j] > min_height:
            visible_trees += 1

print(visible_trees)

max_score = 0
for i in range(1,tree_matrix.shape[0]-1):
    for j in range(1,tree_matrix.shape[1]-1):
        view1 = np.where(tree_matrix[0:i,j][::-1]>=tree_matrix[i,j])[0]
        view2 = np.where(tree_matrix[i,0:j][::-1]>=tree_matrix[i,j])[0]
        view3 = np.where(tree_matrix[i,j+1:]>=tree_matrix[i,j])[0]
        view4 = np.where(tree_matrix[i+1:,j]>=tree_matrix[i,j])[0]
        view1 = len(tree_matrix[0:i,j][::-1]) if len(view1) == 0 else view1[0]+1
        view2 = len(tree_matrix[i,0:j][::-1]) if len(view2) == 0 else view2[0]+1
        view3 = len(tree_matrix[i,j+1:]) if len(view3) == 0 else view3[0]+1
        view4 = len(tree_matrix[i+1:,j]) if len(view4) == 0 else view4[0]+1
        
        score = view1 * view2 * view3 * view4
        if score > max_score:
            max_score = score
print(max_score)