from matplotlib import pyplot as plt 

varians = [1, 2, 4, 8, 16, 32, 64, 128, 256] # Дисперсия
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1] # Квадрат смещения

# Суммарная ошибка
total_error = [x + y for x, y in zip(varians, bias_squared)]
xs = [i for i, _ in enumerate(varians)]

plt.plot(xs, varians, 'g-', label="дисперсия")
plt.plot(xs, bias_squared, 'r-.', label="смещение^2")
plt.plot(xs, total_error, 'b:', label="суммарная ошибка")

plt.legend(loc=9)
plt.xlabel("Сложность модели")
plt.title("Компромис между смещением и дисперсией")

plt.show()
