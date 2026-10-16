import numpy as np
from dataclasses import dataclass

@dataclass
class Neighbours:
    left: int
    right: int
    up: int
    down: int

@dataclass
class SystemParams:
    T: float
    J: float
    h: float
    k_b: float = 1

class Lattice:
    def __init__(
            self,size=(10,10),
            neighbours=1,
            initial_state='random',
            system = None,
            seed=123
    ):

        self.size = size
        self.neighbours = neighbours
        self.rng = np.random.default_rng(seed)
        self.system = system

        if initial_state == 'random':
            self.lattice = self.rng.choice([-1, 1], size=size,)

    def __call__(self):
        return self.lattice

    def move(self,i,j,value):
        if value not in [-1,1]:
            raise ValueError('Invalid value for spin')
        self.lattice[i,j]=value

    def get_neighbours(self,i,j):
        return Neighbours(
            left=self.lattice[i, (j - 1) % self.size[1]],
            right=self.lattice[i, (j + 1) % self.size[1]],
            up=self.lattice[(i - 1) % self.size[0], j],
            down=self.lattice[(i + 1) % self.size[0], j]
        )
    def flip(self,i,j):
        self.lattice[i,j]*=-1

    def magnetization(self):
        return self.lattice.mean()

