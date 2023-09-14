from typing import List
import math

Vector = List[float]

height_weight_age = [175,
                        68,
                        40]

grades = [95,
          80,
          75,
          62]

def add(v: Vector, w: Vector) -> Vector:
    """Складывает соответствующие элементы"""
    assert len(v) == len(w), "Векторы должны иметь одинаковую длину"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

#print(add([1, 2, 3], [4, 5, 6]))

def subtract(v: Vector, w: Vector) -> Vector:
    """Вычитает соответствующие элементы"""
    assert len(v) == len(w), "Векторы должны иметь одинаковую длину"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

#print(subtract([5, 7, 9], [4, 5, 6]))

def vector_sum(vectors: List[Vector]) -> Vector:
    """Суммирует все соответствующие векторы"""
    # Проверить, что векторы не пустые
    assert vectors, "векторы не представлены"

    # Проверить, что векторы имеют одинаковый размер
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Разные размеры"

    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

#print(vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]))
def scalar_multiply(c: float, v: Vector) -> Vector:
    """Умножает каждый элемент на с"""
    return [c * v_i for v_i in v]

#print(scalar_multiply(2, [1, 2, 3]))

def vector_mean(vectors: List[Vector]) -> Vector:
    """Выражает поэлементное среднее арифметическое"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

#print(vector_mean([[1, 2], [3, 4], [5, 6]]))

def dot(v: Vector, w: Vector) -> float:
    """Вычисляет v_1 * w_1 + v_2 * w_2 + ... + v_n * w_n"""
    assert len(v) == len(w), "Векторы должны иметь одинаковую длину"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

#print(dot([1, 2, 3], [4, 5, 6]))

def sum_of_squares(v: Vector) -> float:
    """Возвращает v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

#print(sum_of_squares([1, 2, 3]))
def magnitude(v: Vector) -> float:
    """Возвращает магнитуду (или длину) вектора v"""
    return math.sqrt(sum_of_squares(v))

def distance(v: Vector, w: Vector) -> Vector:
    return magnitude(subtract(v, w))

