import numpy as np

#ближайшие соседи
base_mask = np.array([
    [0,1,0],
    [1,0,1],
    [0,1,0]
])
diagonal_mask = np.array([
    [1,0,1],
    [0,0,0],
    [1,0,1]
])