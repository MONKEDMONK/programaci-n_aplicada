a = input("ingresa un numero a: ")
a = int(a)
b = input("ingresa un numero b: ")
b = float(b)
c = a + b

if a == b:
    print("iguales")
else:
    print("Diferentes")

print("a es tipo: ", type(a))
print("b es tipo: ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("a y b son del mismo tipo")
else:
    print("a y b son de  de diferntes tipos")
