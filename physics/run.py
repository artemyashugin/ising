from physics.metropolis import sweep
from dataclasses import dataclass, field
from physics.hamiltonian import energy

@dataclass
class Params:
    energy: list[float] = field(default_factory=list)
    magnetization: list[float] = field(default_factory=list)

def run(
        lattice,
        N=1000):

    for _ in range(N):
        sweep(lattice)
'''
    p = Params()

    p.energy.append(energy(lattice))
    p.magnetization.append(lattice.magnetization())
'''

'''
        p.energy.append(energy(lattice))
        p.magnetization.append(lattice.magnetization())
    return p
'''


