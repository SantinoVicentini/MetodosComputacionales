import numpy as np
import matplotlib.pyplot as plt
from typing import List

#1)
def suma(vec1:List[int], vec2:List[int]) -> List[int]:
    vr:List[int] = []
    i:int = 0
    while i < len(vec1):
        if len(vec1) == len(vec2):
            vr.append(vec1[i]+vec2[i])
        i+=1
    return vr

print(suma([1,2,3], [2,2]))

def resta(vec1:List[int], vec2:List[int]) -> List[int]:
    vr:List[int] = []
    i:int = 0
    while i < len(vec1):
        if len(vec1) == len(vec2):
            vr.append(vec1[i]-vec2[i])
        i+=1
    return vr

print(resta([1,2,3], [2,2,5]))

def productoEscalar(vec1:List[int], vec2:List[int]) -> int:
    vr:int= 0
    i:int = 0
    while i < len(vec1):
        if len(vec1) == len(vec2):
            vr = vr + (vec1[i] * vec2[i])
        i+=1
    return vr

print(productoEscalar([1,2,3], [2,2,5]))

#2
def sumaMatrices(matr1, matr2) -> List[List[int]]:

