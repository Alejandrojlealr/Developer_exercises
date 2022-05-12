# Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
# edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
# elementos. retornar la lista.

from random import randint

def lista_diccionario():
    lista=[]
    while len(lista) < 10:
         diccionario = {'id': randint(0,25), 'Edad':randint(1,100)}
         lista.append(diccionario)
    return lista

print('Lista de diccionarios \n', lista_diccionario())

# Hacer otra función que reciba lo generado en la primera función y ordenarlo de mayor a
# menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.

def ordenar_lista():
    lista_ordenada = sorted(lista_diccionario(), key=lambda e: e['Edad'], reverse=True)
    id1 = lista_ordenada[0]
    id2= lista_ordenada[-1]
    
    print('El ID de la persona de mayor edad es: ', list(id1.values())[0])
    print('El ID de la persona de menor edad es: ', list(id2.values())[0])
    print('Esta es una lista ordenada decreciente por edad: \n' , lista_ordenada)
    
print(ordenar_lista())