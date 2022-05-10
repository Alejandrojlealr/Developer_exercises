#Crear una matriz de 5x5 randomizada con numeros enteros, encontrar secuencia de 4 numeros consecutivos horizontal
# o vertical y si se encuentra mostrar la posicion incial y final.

from random import randint
import numpy as np
#from numpy import random as rd

matriz2 = np.arange(25).reshape(5,5)
print('Matriz de numeros consecutivos''\n', matriz2)
lista_matriz = matriz2.tolist()
print(f' Lista matriz numeros consecutivos: {lista_matriz}')


for x in (lista_matriz):
  #print(x)
  if x[1] - x[0] == 1 and x[2] - x[1] == 1 and x[3] - x[2] == 1 and x[4] - x[3] == 1:
    print(x)
    print('Lista consecutiva')
    print('Posicion de numero maximo: ' , x.index(max(x)), '/  Posicion de numero minimo: ' , x.index(min(x)))
  else:
    print('lista no consecutiva')