while True:

    value = int(input("Ingrese un valor entero positivo : "))
    print("Value: ", value)
    a = isinstance(value, int)
    if a == True and value > 0:
        fact = 1
        for i in range (1, value + 1):
            fact = fact*i            
        print("El factorial de ",{value}, "is": ', fact)
    else:
        print("porfavor, ingrese un numero positivo entero")
