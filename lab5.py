"""Zadanie 1"""
A = {1/x for x in range(1, 11)}
B = {2**x for x in range(11)}
C = {x for x in B if x % 4 == 0}
print(A, B, C, sep='\n')

"""Zadanie 2"""
import random

macierz = [[random.random() for _ in range(4)] for _ in range(4)]
glowna_przekatna = [macierz[i][i] for i in range(4)]


print("Macierz:")
for wiersz in macierz:
    print(wiersz)

print("\nGłówna przekątna:")
print(glowna_przekatna)

"""Zadanie 3"""
text = "Ala ma kota."
result = [(word, [ord(char) for char in word]) for word in text.split()]
print(result)

"""Zadanie 4"""
import math
from typing import Union, Tuple

def row_kwadratowe(a: float, b: float, c: float) -> Union[float, Tuple[float, float]]:
    delta = b**2 - 4 * a * c
    if delta < 0:
        return -1
    elif delta == 0:
        x = (-b) / (2 * a)
        return x
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))

"""Zadanie 5"""
from typing import List, Tuple
import random

def rzut_kostka(n: int) -> List[Tuple[str, int]]:
    results = [0] * 6
    for _ in range(n):
        result = random.randint(1, 6)
        results[result - 1] += 1
    return [(f'oczka: {i+1}', f'rzutów: {count}') for i, count in enumerate(results)]

print(rzut_kostka(100))

"""Zadanie 6"""
def ciag(* lancuchy):
    if len(lancuchy) == 0:
        return []
    else:
        return sorted(lancuchy)

print(ciag())
print(ciag("banana", "apple", "kiwi", "grape", "fig", "date", "cherry"))

"""Zadanie 7"""
def zlicz(**druzyna: int) -> int:
    return sum(druzyna.values())
print(zlicz(Barcelona=3, RealMadryt=2, Liverpool=5))
