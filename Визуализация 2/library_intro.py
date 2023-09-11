from matplotlib import pyplot as plt 

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] # Годы
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3] # ВВП

# Сздать линейную диаграмму: годы по оси х, ВВП по у
plt.plot(years, gdp, color="green", marker="o", linestyle='solid')

# Добавить название диаграммы
plt.title("Номинальный ВВП")

# Добавить подпись к оси y
plt.ylabel("Млрд $")
plt.show()