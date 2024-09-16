import numpy as np
import matplotlib.pyplot as plt

# Настройка параметров системы
n_particles = 1000
box_size = 10
temperature = 1.0
mass = 0.001

# Инициализация массива частиц
particles = np.random.uniform(low=0, high=box_size, size=(n_particles, 2))

# Цикл по времени
for t in range(1000):

    # Для каждой частицы
    for i in range(n_particles):

        # Найти направление движения частицы
        direction = np.random.uniform(low=0, high=2 * np.pi)

        # Найти шаг частицы
        step = np.sqrt(2 * temperature / mass)

        # Обновить положение частицы
        particles[i, :] += step * np.cos(direction), step * np.sin(direction)

    # Отобразить систему
    plt.scatter(particles[:, 0], particles[:, 1], s=1, c='b')
    plt.pause(0.01)

plt.show()
#Эта программа визуализирует движение 1000 частиц в коробке размером 10 на 10. Частицы движутся случайно, и их скорость меняется в зависимости от температуры системы. Чем выше температура, тем быстрее движутся частицы.