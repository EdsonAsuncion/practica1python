propina=0
consumo=float(input("cuanto fue su consumo en el restaurante"))
porcentaje=float(input("cuanto es el porcentaje que desea dejar de propina"))

if porcentaje>=15:
    
    propina= consumo*porcentaje/100
    print(f"la cantidad de dinero que se dejo de propina fue s/{propina}")
else:
    print("el porcentaje  de la propina debe ser mayor o igual al 15%")


