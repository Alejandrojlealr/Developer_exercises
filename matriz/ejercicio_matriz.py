# Crear una matriz de 5x5 randomizada con numeros enteros, encontrar secuencia de 4
# numeros consecutivos horizontal o vertical y si se encuentra mostrar la posicion 
# inicial y final

import numpy as np
import random

# Lista de numeros consecutivos para pruebas
#matriz2 = [[11, 12, 13, 14, 15],[25, 26, 27, 28, 50,], [69, 70, 71, 72, 73], [74, 80, 75, 76, 77], [91, 92, 93, 94, 98]]

matriz = np.random.randint(10,99, size =(5,5))
print(f' Matriz random \n {matriz}')
matriz2 = matriz.tolist() 

contador = 0
for item in matriz2:
  if item[1] - item[0] == 1 and item[2] - item[1] == 1 and item[3] - item[2] == 1 and item[4] - item[3] == 1:
    print('...........................')
    contador = contador + 1
    print(f'Hay Numeros consecutivos en la lista con posicion {contador - 1} {item} ' + 'Posicion del numero maximo: ' , item.index(max(item)), '/  Posicion del numero minimo: ' , item.index(min(item)))
    
  else:
    contador = contador + 1
    print(f'No hay numeros consecutivos en la lista con posicion {contador - 1} de la matriz')



    



