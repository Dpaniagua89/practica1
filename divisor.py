def divisor(dato, x, y):
    if dato %  x == 0 and dato % y == 0:
        print ("es divisible")
    else:
        print ("no es divisible")

dato  = int(input(f"ingrese su dato: "))
x   = int(input(f"ingrese el valor de X: "))
y   = int(input(f"ingrese el valor de Y: "))

resultado = divisor(dato, x, y)