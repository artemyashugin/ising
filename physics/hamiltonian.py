def delta_energy(
        lattice,
        i, j,
):
    spin = lattice.lattice[i, j]
    n = lattice.get_neighbours(i, j)

    neighbors_sum = n.left + n.right + n.up + n.down

    return 2 * spin * (lattice.system.J * neighbors_sum + lattice.system.h)

def energy(
        lattice,
):
    E_J = 0.0
    E_h = 0.0
    for i in range(lattice.size[0]):
        for j in range(lattice.size[1]):
            spin = lattice.lattice[i, j]
            n = lattice.get_neighbours(i, j)
            E_J+= spin * (n.right + n.down)
            E_h += spin
    return -lattice.system.J * E_J - lattice.system.h * E_h