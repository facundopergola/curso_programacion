# Solicitar al usuario que ingrese dos números y
# mostrar cuál de los dos es menor. No considerar el caso en que ambos números son iguales.

# Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor.
# Considerar el caso en que ambos números son iguales

a=input("ingrese un numero:")
b=input("ingrese otro numero:")
if (a>b):
    print("el primer numero es mayor")
elif (b>a):
    print("el segundo numero es mayor")
else:
    print("los numeros son iguales")
    



#Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
#otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. 
#Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

dia=input(("Ingrese un dia de la semana: "))
if (dia=="lunes"):
    print("el lunes sale futbol con los pibes")
if (dia=="viernes"):
    print("el viernes comemos asado")
if (dia=="sabado"):
    print("el finde descanso")
if (dia=="martes"):
    print("el martes y jueves es feriado")
if (dia=="miercoles"):
    print("el miercoles nos conectamos en meet")

#Escribir un programa que, dado un número entero, muestre su valor absoluto. 
#Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, 
#su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

numero=int(input("numero:"))
if numero<0:
    numero=numero*-1
print("valor absoluto:",numero)


#solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables.
#A continuación, imprimir “coincidencia” si los nombres de ambas personas 
#comienzan con la misma letra ó si terminan con la misma letra. Si no es así, imprimir “no hay coincidencia”.

nombre1=input("ingrese un nombre:")
nombre2=input("ingrese otro nombre:")
posicion_final_nombre1=len(nombre1)-1
posicion_final_nombre2=len(nombre2)-1
if nombre1[0]== nombre2[0] or nombre1[posicion_final_nombre1]== nombre2[posicion_final_nombre2]:
    print("coincidencia")
else:
    print("no hay coincidencia")

#Crear un programa que permita al usuario elegir un candidato por el cual votar. 
#Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, 
#candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje 
#“Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario 
#ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”

candidato1=input("candidato elegido:")
if candidato1.upper()== "A":
    print("usted ha elegido el candidato Rojo")
elif candidato1.upper()== "B":
    print("usted ha votado el candidato Azul")
elif candidato1.upper()== "C" :
    print("usted ha votado el candidato Verde")
else:
    print("opcion erronea")


#Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. 
#Se debe validar que el usuario ingrese sólo un carácter. 
 #Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.

letra=input("Letra:")
if len(letra)!=1:
    print("Debe ser sólo una letra")

if letra in "aeiou":
        print("Es vocal")
else:
    print("no es una vocal")





