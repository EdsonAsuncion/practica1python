show=int(input("cuantos show musicales ha visto en el último año"))
if show==0:
    print(f"el valor es: {bool(show)}")
elif show==1:
    print(f"el valor es: {bool(show-1)}")
elif show==2:
    print(f"el valor es: {bool(show-2)}")
elif show==3:
    print(f"el valor es: {bool(show-3)}")
else:
     print(f"el valor es: {bool(show)}")    