# parte de los impares
for i in range (1,21):
     residual = i%2
     if residual == 0:
         print( i," is even")
     else:
         #print('{i} is odd')
         print(str(i) + ' is odd')
# contador con multiplicado
for i in range (1,6):
     result = i**3
     print(result)
#contador hasta el numero ingresado excepto 0
times = input("Enter a number of times: ")
times = float(times)
times = int(times)
print(type(times))
print(times)

if times == 0:
    print("Don't do anything")
else:
    for i in range(1,times+1):
        print("i = ", i)
