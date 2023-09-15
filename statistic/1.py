from collections import Counter
import matplotlib.pyplot as plt
from typing import List

num_friends = [98, 24, 63, 31, 41, 86, 74, 85, 59, 32, 31, 48, 9, 98, 50, 73, 25, 27, 47, 90, 56, 54, 78, 17, 33, 42, 66, 48, 4, 76, 93, 34, 25, 
    80, 31, 13, 65, 13, 43, 82, 17, 76, 65, 36, 9, 90, 91, 71, 54, 64, 86, 86, 52, 13, 100, 3, 74, 51, 36, 2, 58, 68, 70, 84, 72, 15, 3, 1, 13, 42, 
    15, 82, 62, 40, 63, 94, 85, 27, 52, 40, 8, 66, 97, 94, 98, 75, 23, 32, 19, 18, 62, 23, 38, 73, 17, 14, 53, 42, 3, 100, 8, 79, 95, 51, 40, 65, 54, 
    79, 1, 51, 10, 55, 98, 67, 9, 4, 15, 62, 67, 95, 59, 76, 23, 37, 18, 2, 69, 55, 70, 96, 10, 81, 89, 49, 29, 44, 2, 41, 88, 19, 29, 76, 95, 75, 70, 
    74, 65, 21, 79, 2, 13, 96, 88, 44, 19, 72, 80, 96, 48, 5, 11, 48, 2, 74, 56, 38, 26, 100, 28, 92, 73, 11, 26, 36, 45, 83, 98, 52, 5, 13, 44, 4, 14, 
    4, 49, 75, 12, 26, 39, 49, 24, 37, 19, 7, 16, 38, 35, 65, 57, 95, 59, 
    47, 96, 12, 81, 26, 28, 83, 25, 83, 5, 54, 47, 42, 90, 73, 84, 58, 9, 23, 4, 22, 3, 46, 97, 77, 69, 96, 64, 74, 96, 74, 31, 89, 35, 55, 13, 58, 14, 
    66, 16, 67, 54, 44, 50, 57, 26, 6, 52, 2, 74, 66, 52, 55, 13, 70, 24, 54, 78, 39, 28, 59, 74, 7, 86, 58, 54, 32, 79, 16, 88, 88, 15, 72, 14, 6, 5, 90, 6, 
    85, 16, 58, 9, 78, 51, 36, 55, 31, 85, 63, 93, 67, 61, 73, 28, 21, 73, 42, 75, 22, 90, 44, 
    6, 28, 18, 96, 17, 92, 60, 15, 50, 19, 24, 55, 29, 43, 91, 17, 47, 23, 4, 29, 100, 76, 60, 98, 46, 62, 91, 36, 77, 84, 50, 98, 78, 
    38, 79, 14, 26, 46, 42, 16, 57, 99, 93, 29, 15, 1, 11, 40, 87, 41, 89, 4, 4, 73, 94, 38, 98, 5, 75, 19, 41, 
    34, 89, 23, 4, 32, 100, 56, 14, 49, 3, 56, 63, 84, 36, 28, 46, 35, 89, 87, 4, 29, 33, 41, 98, 37, 41, 69, 15, 
    82, 34, 36, 78, 76, 57, 4, 3, 96, 84, 24, 40, 21, 48, 64, 37, 23, 76, 53, 100, 58, 20, 73, 26, 83, 9, 73, 77, 15, 49, 75, 40, 91, 50, 40, 88, 95, 34, 
    70, 56, 13, 30, 92, 49, 61, 27, 2, 78, 1, 31, 57, 29, 91, 42, 40, 36, 70, 78, 15, 29, 97, 31, 50, 54, 95, 21, 81, 11, 88, 28, 21, 31, 18, 32, 54, 29, 31, 
    20, 7, 28, 5, 67, 32, 99, 78, 46, 57, 11, 6, 10, 97, 31, 56, 12, 9, 25, 83, 49, 22, 1, 43, 36, 41, 40, 76, 45, 94, 25, 7, 64, 57, 17, 38, 19, 82, 40, 68, 
    64, 15, 88, 99, 21, 99, 10, 57, 83, 17, 60, 55, 24, 42, 57, 36, 70, 18, 67, 13, 27, 23, 24, 53, 87, 75, 72, 28, 28, 93, 34, 12, 74, 95, 23, 46, 27, 42, 16, 
    100, 40, 3, 69, 100, 93, 47, 72, 75, 89, 80, 25, 100, 70, 63, 95, 53, 98, 18, 4, 83, 
    12, 20, 61, 14, 96, 61, 19, 45, 47, 3, 10, 59, 60, 29, 73, 3, 38, 72, 30, 98, 11, 42, 2, 27, 85, 88, 44, 74, 
    44, 13, 38, 90, 30, 54, 37, 24, 58, 17, 53, 78, 29, 33, 39, 2, 73, 98, 96, 36, 64, 17, 56, 73, 40, 1, 53, 11, 1, 6, 72, 30, 84, 33, 1, 84, 79, 63, 100, 
    44, 33, 67, 99, 90, 76, 7, 51, 22, 96, 41, 45, 2, 94, 100, 87, 72, 33, 36, 42, 9, 87, 70, 98, 86, 99, 32, 26, 39, 13, 72, 33, 58, 60, 24, 69, 80, 76, 86, 
    3, 99, 4, 59, 98, 66, 76, 84, 9, 94, 93, 51, 31, 25, 74, 20, 51, 100, 5, 96, 84, 67, 55, 81, 75, 81, 35, 11, 
    41, 80, 13, 73, 25, 34, 5, 85, 24, 98, 22, 33, 7, 63, 97, 22, 76, 84, 33, 95, 22, 79, 96, 58, 60, 55, 28, 55, 29, 60, 51, 100, 93, 
    40, 72, 86, 84, 90, 18, 4, 8, 7, 81, 26, 36, 77, 28, 26, 87, 72, 55, 20, 5, 92, 65, 15, 98, 11, 98, 54, 25, 71, 85, 17, 36, 6, 6, 60, 97, 56, 62, 
    40, 71, 68, 72, 100, 22, 31, 76, 54, 14, 99, 2, 4, 22, 12, 99, 24, 29, 24, 32, 23, 25, 71, 25, 94, 87, 15, 72, 10, 22, 82, 8, 65, 15, 11, 87, 18, 32, 3, 67, 97, 16, 79, 60, 54, 56, 37, 77, 47, 8, 39, 52, 22, 83, 50, 12, 20, 27, 82, 30, 17, 78, 51, 19, 77, 62, 21, 93, 49, 53, 4, 60, 8, 4, 24, 72, 9, 50, 92, 28, 43, 27, 1, 33, 65, 17, 22, 96, 24, 24, 23, 85, 52, 69, 62, 95, 100, 28, 54, 16, 37, 97, 92, 13, 6, 58, 4, 39, 76, 16, 90, 95, 11, 25, 3, 58, 41, 83, 21, 44, 63, 66, 75, 91, 76, 93, 86, 87, 29, 99, 
    48, 98, 42, 6, 25, 5, 33, 57, 10, 52, 13, 44, 86, 73, 35, 43, 31, 19, 26, 46, 84, 9, 32, 17, 57, 73, 26, 96, 94, 23, 43, 53, 67, 16, 85, 21, 64, 46, 30, 76, 86, 14, 3, 56, 52, 83, 60, 18, 67, 13, 29, 72, 82, 100, 46, 87, 25, 18, 77, 71, 97, 52, 56, 9, 19, 58, 61, 14, 20, 74, 74, 11, 76, 43, 9, 19, 62, 89, 52, 18, 96, 59, 76, 58, 4, 2, 44, 13, 97, 81, 90, 93, 16, 78, 99, 42]

friend_counts = Counter(num_friends)

xs = range(101)
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])

plt.title("Гистограмма количеств друзей")
plt.xlabel("Число друзей")
plt.ylabel("Число людей")

# plt.show()
num_points = len(num_friends) # Число точек равно 999
largest_value = max(num_friends) # Наибольшее значение 100
smallest_value = min(num_friends) # Наименьшее значение равно 1

sorted_values = sorted(num_friends) # Отсортированные значения

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

# print(mean(num_friends)) # 49.434434434434436
def _median_odd(xs: List[float]) -> float:
    """если длина нечетная - то медиана средний элемент"""
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
    """если длина четная - то медиана среднее значение двух срединных элементов"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
    """Отыскивает близжайшее к середине значение v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

# print(median([1, 10, 2, 9, 5]))
# print(median([1, 9, 2, 10]))
# print(median(num_friends))

def quantile(xs: List[float], p: float) -> float:
    """ Возвращает значение p-ого процента в x """
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


# print(quantile(num_friends, 0.10))
# print(quantile(num_friends, 0.25))
# print(quantile(num_friends, 0.75))
# print(quantile(num_friends, 0.90))

def mode(x: List[float]) -> List[float]:
    """ Возвращает список, т.к. может быть больше одной моды """
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

# print(set(mode(num_friends))) # 4
def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

print(data_range(num_friends)) # 99