import numpy as np

def create_kernel(*args):
    all_masks = [mask for mask in args]
    max_mask = max(all_masks,key = lambda mask: mask.size)
    max_size = len(max_mask)

    kernel = np.zeros((max_size, max_size), dtype=float)
    for mask in all_masks:
        pad = (max_size-len(mask))//2
        mask = np.pad(mask, pad_width=pad, mode='constant', constant_values=0)
        kernel += mask

    return kernel

#ближайшие соседи
base_kernel = np.array([
    [0,1,0],
    [1,0,1],
    [0,1,0]
])
diagonal_mask = np.array([
    [1,0,1],
    [0,0,0],
    [1,0,1]
])