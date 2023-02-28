def imorimir(arreglo):
  for i in range(len(arreglo)-1):
    print(f'[{arreglo[i]}]',end="")
  print()

def burbuja(arreglo):
  for i in range(len(arreglo)-1):
    for j in range(len(arreglo)-1-i):
      if arreglo[j] > arreglo[j+1]:
        aux=arreglo[j]
        arreglo[j]=arreglo[j+1]
        arreglo[j+1]=aux

listasueldos=[20,15,161,21,55,14,5,23,56,797,75,160]
print("parte sin modificar")
imorimir(listasueldos)
burbuja(listasueldos)
print("parte con metodo burbuja")
imorimir(listasueldos)