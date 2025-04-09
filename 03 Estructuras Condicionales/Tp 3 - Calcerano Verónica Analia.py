#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int (input("Ingresu su edad: "))
if (edad >= 18):
    print ("Es mayor de edad")
    #No está solicita pero se puede agregar
else:
    print ("No es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float (input("Ingrese su nota "))
if (nota >= 6):
    print ("Aprobado")
else:
    print ("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, 
#  imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del# operador de módulo (%) en Python para evaluar si un número es par o impar.


#se podría ejecutar while para que vuelva a solicitar un número

numero = int(input("Ingrese un número: "))

while numero % 2 != 0:
    numero= int(input("Por favor, ingrese un número par"))

print("Ha ingresado un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad_2 = int (input("Indique su edad: "))

if edad_2 < 12:
    print("Según su edad, ústed pertenece a la categoría de niño")
elif edad_2 >= 12 and edad_2 < 18:
    print("Según su edad, ústed pertenece a la categoría de adolescente")
elif edad_2 >= 18 and edad_2 < 30:
    print("Según su edad, ústed pertenece a la categoría de adulto/a joven")
elif edad_2 >= 30:
    print("Según su edad, ústed pertenece a la categoría de adulto/a")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, 
# imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("Ingresa una constrasena: ")
while len (contraseña) < 8 or len (contraseña) > 14:
    contraseña = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")
print ("Ha ingresado una constraseña correcta")


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print (numeros_aleatorios)

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)


if media > mediana > moda:
    print ("Hay sesgo positivo")
elif media < mediana < moda:
    print ("Hay sesgo negativo")
else:
    print ("No hay sesgo negativo")  

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input ("Ingrese una frase o palabra: ").strip()
if frase [-1] in "aeiouAEIOU":
    print (frase + "!")
else:
    print (frase) 

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.

nombre = input("Ingrese su nombre: ")
print ("Seleccione: ") 
print ("1. Si quiere su nombre en mayúsculas.")
print ("2. Si quiere su nombre en minúsculas. ")
print ("3. Si quiere su nombre con la primera letra mayúscula. ")

opcion = input("Ingrese la opción deseada: " )

if opcion == "1":
    print (nombre.upper()) #CONVIERTE EN MAYUSCULA
elif opcion == "2":
    print (nombre.lower()) #CONVIERTE EN MINUSCULA
elif opcion == "3":
    print (nombre.title()) #CONVIERTE EN MAYUSCULA LA PRIMERA
else:
    print ("El número ingresado no es una opción válida.")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter 
# e imprima el resultado por pantalla:

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
        print ('"Muy leve" (imperceptible)') # Usar el uso de comillas simples para delimitar, permite que las comillas dobles se muestren.
elif magnitud >= 3 and magnitud < 4:
    print ('"Leve" (ligeramente perceptible)')
elif magnitud >= 4 and magnitud < 5:
    print ('"Moderado" (sentido por personas, pero generalmente no causa daños)')
elif magnitud >= 5 and magnitud < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles)')
elif magnitud >= 6 and magnitud < 7:
    print ('"Muy Fuerte" (puede causar daños significativos)')
elif magnitud >= 7:
    print('"Extremo" (puede causar graves daños a gran escala)') 

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

print ("En que hemisferio se encuentra: ")
hemisferio = input ("N o S?: ")
mes = int (input("Ingrese en números, que mes del año es?: "))
dia = int (input ("Ingrese que día es: "))

hemisferio = hemisferio.lower()

while (mes > 12):
    print ("El dato ingresado para el mes no es válido")
    mes = int (input("Ingrese en números, que mes del año es?: "))

while mes in (1, 3, 5, 7, 8, 10, 12) and (dia > 31):
    print ("Este solo tiene 31 días.")
    dia = int (input ("Ingrese que día es: "))

while mes in (4, 6, 9, 11) and (dia > 30):
        print ("Este mes solo tiene 30 días.")
        dia = int (input ("Ingrese que día es: "))

while (mes == 2) and (dia > 29):
        print ("Este mes tiene como máximo 29 días.")
        dia = int (input ("Ingrese que día es: "))

if hemisferio == "n":
    if (mes == 12 and (dia > 20 and dia <= 31)) or (mes == 1 or mes == 2) or mes == 3 and (dia <= 20):
        print ("Invierno")
    elif (mes == 3 and (dia >= 21 and dia <= 31)) or (mes == 4 or mes == 5) or mes == 6 and (dia <= 20):
        print ("Primavera")
    elif (mes == 6 and (dia >= 21 and dia <= 31)) or (mes == 7 or mes == 8) or mes == 9 and (dia <= 20):    
        print ("Verano")
    elif (mes == 9 and (dia >= 21 and dia <= 31)) or (mes == 10 or mes == 11) or mes == 12 and (dia <= 20):    
        print ("Otoño")

if hemisferio == "s":
    if (mes == 12 and (dia > 20 and dia <= 31)) or (mes == 1 or mes == 2) or mes == 3 and (dia <= 20):
        print ("Verano")
    elif (mes == 3 and (dia >= 21 and dia <= 31)) or (mes == 4 or mes == 5) or mes == 6 and (dia <= 20):
        print ("Otoño")
    elif (mes == 6 and (dia >= 21 and dia <= 31)) or (mes == 7 or mes == 8) or mes == 9 and (dia <= 20):    
        print ("Invierno")
    elif (mes == 9 and (dia >= 21 and dia <= 31)) or (mes == 10 or mes == 11) or mes == 12 and (dia <= 20):    
        print ("Primavera")        