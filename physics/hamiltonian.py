import numpy as np
from numba import njit

@njit
def delta_energy(spins, kernel, h, i, j):
    rows, cols = spins.shape
    kernel_rows, kernel_cols = kernel.shape
    center_i = kernel_rows // 2
    center_j = kernel_cols // 2

    neighbor_field = 0.0

    for ki in range(kernel_rows):
        for kj in range(kernel_cols):
            coupling = kernel[ki, kj]

            if coupling == 0:
                continue

            ni = (i + ki - center_i) % rows
            nj = (j + kj - center_j) % cols

            neighbor_field += coupling * spins[ni, nj]

    return 2 * spins[i, j] * (neighbor_field + h)


@njit
def energy(spins, kernel, h):
    rows, cols = spins.shape
    kernel_rows, kernel_cols = kernel.shape
    center_i = kernel_rows // 2
    center_j = kernel_cols // 2

    E_J = 0.0
    E_h = 0.0

    for i in range(rows):
        for j in range(cols):
            spin = spins[i, j]
            E_h += spin

            for ki in range(kernel_rows):
                for kj in range(kernel_cols):
                    coupling = kernel[ki, kj]

                    if coupling == 0:
                        continue

                    ni = (i + ki - center_i) % rows
                    nj = (j + kj - center_j) % cols

                    E_J += coupling * spin * spins[ni, nj]

    return -0.5 * E_J - h * E_h