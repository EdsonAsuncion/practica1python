edad=int(input("¿cual es tu edad?"))
if edad > 0 and 4>edad:
    print("puede entrar gratis")
elif 18>= edad and edad>=4:
    print("debe pagar $5")
elif edad >18:
    print("debe pagar $10")