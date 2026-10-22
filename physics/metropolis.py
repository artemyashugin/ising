import numpy as np
from physics.hamiltonian import delta_energy
from numba import njit

@njit
def step(spins, kernel, T, h, k_b):
    rows, cols = spins.shape

    i = np.random.randint(rows)
    j = np.random.randint(cols)

    de = delta_energy(spins, kernel, h, i, j)

    if de <= 0:
        spins[i, j] *= -1
    elif T > 0:
        probability = np.exp(-de / (k_b * T))

        if np.random.random() < probability:
            spins[i, j] *= -1


@njit
def sweep(spins, kernel, T, h, k_b):
    rows, cols = spins.shape
    for _ in range(rows * cols):
        step(spins, kernel, T, h, k_b)



