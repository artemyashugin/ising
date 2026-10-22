import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from physics.metropolis import sweep
from matplotlib.widgets import Slider
from collections import deque

def animate(lattice):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    #слайдер температуры
    fig.subplots_adjust(bottom=0.2)

    slider_ax = fig.add_axes([0.2, 0.07, 0.6, 0.04])

    temp_slider = Slider(
        ax=slider_ax,
        label='Temperature',
        valmin=0.1,
        valmax=5.0,
        valinit=lattice.system.T,
        valstep=0.001
    )
    # функция изменения температуры
    def change_temperature(value):
        lattice.system.T = value
    temp_slider.on_changed(change_temperature)

    # слайдер магнитного поля
    mag_ax = fig.add_axes([0.2, 0.02, 0.6, 0.04])

    mag_slider = Slider(
        ax=mag_ax,
        label='Magnetic field',
        valmin=-2.0,
        valmax=2.0,
        valinit=lattice.system.h,
        valstep=0.05
    )

    # функция изменения магнитного поля
    def change_mag(value):
        lattice.system.h = value

    mag_slider.on_changed(change_mag)

    #поле спинов
    image = ax1.imshow(
        lattice.lattice,
        cmap='bwr',
        vmin=-1,
        vmax=1,
        interpolation='nearest'
    )

    #график намагниченности
    window = 10000
    magnetizations = deque([lattice.magnetization()], maxlen=window)
    sweep_count = 0

    line, = ax2.plot([], [], color='blue')

    ax2.set_xlim(0, 100)
    ax2.set_ylim(-1.05, 1.05)
    ax2.set_xlabel('Monte Carlo sweeps')
    ax2.set_ylabel('Magnetization')
    ax2.grid()



    def update(frame):
        nonlocal sweep_count
        for _ in range(100):
            sweep(
                lattice.lattice,
                lattice.system.kernel,
                lattice.system.T,
                lattice.system.h,
                lattice.system.k_b,
                )
            sweep_count += 1
            m = lattice.magnetization()
            magnetizations.append(m)

            image.set_data(lattice.lattice)

            ax1.set_title(
                f"T = {lattice.system.T}, "
                f"m = {lattice.magnetization():.3f}"
            )

            start = sweep_count - len(magnetizations) + 1

            line.set_data(
                range(start, sweep_count + 1),
                list(magnetizations),
            )

            ax2.set_xlim(start, max(start + 100, sweep_count))

        return image,line

    ani = FuncAnimation(
        fig,
        update,
        interval=50,
        blit=False,
        cache_frame_data=False
    )

    ani.sliders = [temp_slider, mag_slider]

    plt.show()

    return ani