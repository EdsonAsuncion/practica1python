muestra= ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

eliminar = [muestra[0], muestra[4], muestra[5]]

for valor in eliminar:
    if valor in muestra:
        muestra.remove(valor)

print(muestra)