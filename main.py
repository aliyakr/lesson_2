
"""
Проект: Анимированная симуляция движения частиц с возможностью столкновений

Описание проекта:
- Частицы перемещаются по полю, имея скорость и размер.
- При столкновении с другими частицами или стенками поля происходит отскок.
- Движение частиц отображается в реальном времени с помощью анимации.

Классы:
1. Particle:
    - Атрибуты:
        - position: координаты (x, y).
        - velocity: скорость (vx, vy).
        - color: цвет частицы.
        - size: радиус частицы.
        - trajectory: список позиций для отслеживания пути.
    - Методы:
        - move(bounds): перемещает частицу с учетом границ.
        - check_wall_collision(bounds): отражает от стен.
        - random_color(): случайный выбор цвета.

2. ParticleSimulator:
    - Атрибуты:
        - particles: список частиц.
        - bounds: границы поля.
        - enable_collisions: включение проверки столкновений.
    - Методы:
        - simulate(steps): перемещает все частицы на заданное количество шагов.
        - check_collisions(): проверяет и обрабатывает столкновения.

Функции:
1. animate_particles(particles, bounds, steps, interval, background_color):
    - Анимирует движение частиц на заданном поле.
"""

from utils.classes import Particle, ParticleSimulator
from utils.functions import animate_particles

def main():
    num_particles = 10
    bounds = (0, 20, 0, 20)
    enable_collisions = True

    simulator = ParticleSimulator(
        num_particles = num_particles,
        step_size = 1.0,
        bounds = bounds,
        enable_collisions = enable_collisions
    )

    particles = simulator.get_particles()

    animate_particles(particles, bounds, 100, 100, 'black')

if __name__ == "__main__":
    main()
    
