
import numpy as np
import random

class Particle:
    def __init__(self, position, velocity=None, color=None, size=0.5):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float) if velocity is not None else np.random.uniform(-1, 1, 2)
        self.trajectory = [self.position.copy()]
        self.color = color if color else self.random_color()
        self.size = size

    def move(self, bounds=(0, 10, 0, 10)):
        self.position += self.velocity
        self.trajectory.append(self.position.copy())
        self.check_wall_collision(bounds)

    def check_wall_collision(self, bounds):
        x_min, x_max, y_min, y_max = bounds
        if self.position[0] <= x_min or self.position[0] >= x_max:
            self.velocity[0] *= -1
        if self.position[1] <= y_min or self.position[1] >= y_max:
            self.velocity[1] *= -1

    @staticmethod
    def random_color():
        colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'black']
        return random.choice(colors)

class ParticleSimulator:
    def __init__(self, num_particles=5, step_size=1.0, bounds=(0, 10, 0, 10), enable_collisions=True):
        self.particles = [Particle(np.random.rand(2) * (bounds[1]-bounds[0])) for _ in range(num_particles)]
        self.bounds = bounds
        self.enable_collisions = enable_collisions

    def simulate(self, steps=10):
        for _ in range(steps):
            for particle in self.particles:
                particle.move(self.bounds)
            if self.enable_collisions:
                self.check_collisions()

    def check_collisions(self):
        n = len(self.particles)
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = self.particles[i], self.particles[j]
                distance = np.linalg.norm(p1.position - p2.position)
                if distance <= (p1.size + p2.size):
                    # Простая модель: меняем направления скоростей
                    p1.velocity, p2.velocity = -p1.velocity, -p2.velocity

    def get_particles(self):
        return self.particles
