from matplotlib import pyplot as plt 
# Неправильный график, вводит в заблуждение

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("Число раз, когда я слышал, как упоминали науку о данных")

plt.ticklabel_format(useOffset=False)

# дезориентация оси у (показывает только то, что выше 500)
plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Посмотрите какой 'огромный' рост")


plt.show()