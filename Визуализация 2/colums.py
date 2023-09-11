from matplotlib import pyplot as plt 

movies = ['Энни Холл', 'Бен-Гур', 'Касабланка', 'Ганди', 'Вестсайдская история']
num_oscars = [5, 11, 3, 8, 10]

# Построить столбцы с левыми Х-координатами [xs] и высотами [num_oscars]
plt.bar(range(1, len(movies)+1), num_oscars)

plt.title("Мои любимые фильмы")
plt.ylabel("Количество наград")

# Пометить ось x название фильмов в центре каждого столбца
plt.xticks(range(1, len(movies)+1), movies)

plt.show()
