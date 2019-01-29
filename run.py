from MiArchivo.miarchivo import *
from clases import *
from combinacion import*

m = MiArchivo()
lista=[]
lista = m.obtener_informacion()
lista = [l.split(";") for l in lista]

lista = lista[1:]

operaciones = OperacionesArchivo()
operaciones.Presentar(lista)
listaEdad=operaciones.ListaEdad(lista)

merge_sort_result = merge_sort(listaEdad)

print("\n")
print(merge_sort_result)


#dado el siguiente una clse para rpresentar cadad linea del archivo luego utilizr unicamente el atributo que represente la edad de cada objeto pra almacenar
#lista ordenar por combinacion para ordenars