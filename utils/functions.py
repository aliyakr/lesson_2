
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate_particles(particles, bounds=(0, 20, 0, 20), steps=100, interval=100, background_color='black'):
    fig, ax = plt.subplots()
    ax.set_xlim(bounds[0], bounds[1])
    ax.set_ylim(bounds[2], bounds[3])
    ax.set_facecolor(background_color)

    scatters = []
    for p in particles:
        scatter, = ax.plot([], [], 'o', color=p.color)
        scatters.append(scatter)

    def init():
        for scatter in scatters:
            scatter.set_data([], [])
        return scatters

    def update(frame):
        for i, p in enumerate(particles):
            p.move(bounds)
            scatters[i].set_data(p.position[0], p.position[1])
        return scatters

    ani = animation.FuncAnimation(fig, update, frames=steps, init_func=init, blit=True, interval=interval)
    plt.show()

def generate_initial_positions_circle(num_particles, radius=5):
    positions = []
    angles = np.linspace(0, 2 * np.pi, num_particles, endpoint=False)
    for angle in angles:
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        positions.append((x, y))
    return positions
