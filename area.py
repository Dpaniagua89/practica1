def calcular(figura, ladoA, ladoB):
    if figura == "rectangulo":
        print ((int(ladoA)) *2 + (int(ladoB) * 2))
    elif figura == "cuadrado":
        print (int(ladoA**2 ))
    else:
        print (f"no es una figura selecionada")

figura  = str(input(f"ingrese su figura: "))
ladoA   = int(input(f"ingrese el ladoA: "))
ladoB   = int(input(f"ingrese el ladoB: "))

resultado = calcular(figura, ladoA, ladoB)


