import numpy as np
from dataclasses import dataclass


@dataclass
class SystemParams:
    T: float
    h: float
    kernel: np.ndarray
    k_b: float = 1.0


class Lattice:
    def __init__(
        self,
        size=(10, 10),
        initial_state="random",
        system=None,
        seed=123,
    ):
        self.size = size
        self.rng = np.random.default_rng(seed)
        self.system = system

        if initial_state == "random":
            self.lattice = self.rng.choice([-1, 1], size=size)
        else:
            raise ValueError("Неизвестное начальное состояние")

    def __call__(self):
        return self.lattice

    def magnetization(self):
        return self.lattice.mean()