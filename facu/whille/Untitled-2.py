"""Solicitar al usuario que ingrese su dirección email. Imprimir
un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
Una dirección se considerará válida si contiene el símbolo 
"""
def validar(email):
    caracterBuscado="@"
    emailValido=False
    for c in email:
        if c==caracterBuscado:
            return True
    return False

 
direccion=input("Tu email: ")
if validar(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")


""""
Solicitar números al usuario hasta que ingrese el cero. 
Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).
"""
def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
        return suma
    return False

 
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    num=int(input("Número a procesar: "))



""""
Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. 
Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
Reutilizar la misma función realizada en el ejercicio 2.
"""
def sumadeDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

 
sumatoria=0
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumadeDigitos(num))
    sumatoria=sumatoria+num
    num=int(input("Número a procesar: "))
print("Sumatoria:", sumatoria)
print("Dígitos:", sumadeDigitos(sumatoria))

""""
Requerir al usuario que ingrese un número entero e informar si es primo o no, 
utilizando una función booleana que lo decida.
"""
def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

 
numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")
    """""
Imprimir todos los números entre el 100 y el 199
"""
for x in range(100,200):
    print(x)

""""
Imprimir os números entre el 5 y el 20, saltando de tres en tres.

"""
for i in range(5,20,3):
    print(i)

"""""

Requerir al usuario que ingrese un número entero positivo
e imprimir todos los números correlativos entre el ingresado por el usuario y uno menos del doble del mismo
"""""
n=int(input("Número: "))
for x in range(n, n*2):
    print(x)

"""""
Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. 
En cada iteración, solicitar al usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números ingresados
"""""
c=int(input("Cantidad de números: "))
total=0
for variable in range(c):
   numero=int(input("Número: "))
   total+=numero
print("Total de la suma:", total)


#Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

frase=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiou":
  if x in frase:
    print(x)