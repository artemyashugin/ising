import matplotlib.pyplot as plt

def plot_lattice(lattice):
    plt.imshow(
        lattice.lattice,
        cmap='bwr',
        vmin=-1,
        vmax=1,
        interpolation='nearest'
    )

    plt.show()

