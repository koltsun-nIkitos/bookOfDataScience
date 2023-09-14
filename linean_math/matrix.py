from typing import List
from typing import Tuple
from typing import Callable

Matrix = List[List[float]]
Vector = List[float]

A = [[1, 2, 3],
      [4, 5, 6]]

B = [[1, 2],
      [3, 4],
      [5, 6]]

def shape(A: Matrix) -> Tuple[int, int]:
    """Возвращает число строк А, число стобцов А"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

#print(shape([[1, 2, 3], [4, 5, 6]]))

def get_row(A: Matrix, i: int) -> Vector:
    """Возвращает i-ю строку A как вектор"""
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """Возвращает j-столбец А как вектор"""
    return [A_i[j] for A_i in A]

def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    """
      Возвращает матрицу размера num_rows * num_cols
      чей (i, j)-й элемент является функцией entry_fn(i, j)
    """
    return [[entry_fn(i, j)
              for j in range(num_cols)]
              for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
  """ 
  Возвращает (n*n) матрицу тождественности (единичную)
  """
  return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

print(identity_matrix(5))
