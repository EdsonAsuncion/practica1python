suma=0
numero=int(input("introduzca un numero entero positivo"))

if numero>0:
    suma= numero*(numero+1)/2
    print(f"la suma de todo los enteros desde 1 hasta {numero} es igual a {suma}")
else:
    print("el numero debe ser positivo por favor vuelva a escribir el numero")