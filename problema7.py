primero=float(input("introduce el 1er numero\t"))
segundo=float(input("introduce el 2do numero\t"))
opciones=input("escoja una de la opciones: \n a si desea sumar los numeros\n b si desea restar los numeros \n c si desea multiplicar los numeros\n")
resultado=0
if opciones=="a":
    resultado=primero+segundo
    print(f"la suma de los numeros es {resultado}")
elif opciones=="b":
    resultado=primero-segundo
    print(f"la diferencia de los numeros es {resultado} ")
elif opciones=="c":
    resultado=primero*segundo
    print(f"el producto de los numeros es {resultado}")
else:
    print("no es una opción valida ")
