import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

def monte_carlo_simulation(func, a, b):
    """Оцінка інтеграла методом Монте-Карло."""

    # Генеруємо масиви випадкових чисел
    points = 1000000
    x_random = np.random.uniform(a, b, points)
    y_random = np.random.uniform(0, func(b), points)

    # Підрахунок точок під кривою
    under_curve = y_random <= func(x_random)
    M = np.sum(under_curve)

    # Обчислення площі
    area_rectangle = (b - a) * func(b)
    area = (M / points) * area_rectangle

    return area

# Виконання симуляції
monte_carlo_result = monte_carlo_simulation(f, a, b)
print("Оцінка інтеграла методом Монте-Карло: ", monte_carlo_result)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Обчислення інтеграла
result, error = spi.quad(f, a, b)
print("Інтеграл: ", result, error)
