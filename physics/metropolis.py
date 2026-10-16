import numpy as np
from physics.hamiltonian import delta_energy

def step(
        lattice
):
    rng = lattice.rng

    i = rng.integers(0,lattice.size[0])
    j = rng.integers(0,lattice.size[1])

    de = delta_energy(lattice, i, j)

    if de <= 0:
        lattice.flip(i,j)
    else:
        prob = np.exp(-de/(lattice.system.T*lattice.system.T*lattice.system.k_b))
        if rng.random() < prob:
            lattice.flip(i, j)

def sweep(
        lattice
):
    for _ in range(lattice.size[0]*lattice.size[1]):
        step(lattice)



