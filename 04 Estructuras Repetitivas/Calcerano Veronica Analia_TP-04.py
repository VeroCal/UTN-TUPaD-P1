# **Ejercicio 1**

# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.


for i in range (0,101):
    print(i)

# **Ejercicio 2**

# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.


numero = int (input ("Ingrese un número entero: "))
digitos = len(str(numero))
print(f"Se ingresaron {digitos} digitos")

#### **Ejercicio 3**

# Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.


num1 = int (input ("Ingrese un número entero: "))
num2 = int (input ("Ingrese otro número entero: "))
suma = 0

while num2 < num1:
    print ("El segundo número ingresado debe ser mayor al primero")
    num2 = int (input ("Ingrese otro número entero: "))

for i in range (num1 + 1, num2):
    suma += i

print (f"La suma de los números enteros comprendidos entre los dos valores dados es {suma}")

#### **Ejercicio 4**

# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num = int (input ("Ingrese un número entero, para salir ingrese 0: "))
suma = 0

while num != 0:
    suma += num
    num = int (input ("Ingrese un número entero, para salir ingrese 0: "))

print (f"La suma de los números ingresados es {suma}")

### **Ejercicio 5**

# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random
numero_secreto = random.randint(0,9)
intento = 1
adivinanza = None  # Inicializamos la variable fuera del bucle

adivinanza = int(input("Estoy pensando un número entre el 0 y el 9. Adiviná cuál es: "))

while adivinanza != numero_secreto:
    intento += 1

    if adivinanza < numero_secreto:
        adivinanza = int(input("Demasiado bajo. Probá con un número más alto: "))

    elif adivinanza > numero_secreto:
        adivinanza = int(input("Demasiado alto. Probá con un número más bajo: "))

if adivinanza == numero_secreto:
    print(f"¡Felicitaciones! Adivinaste el número en {intento} intentos.")

#### **Ejercicio 6**

# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.


for i in range (100,-1,-2):
    print(i)

#### **Ejercicio 7**

# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int (input ("Ingrese un número positivo: "))
suma = 0

while num <= 0:
    print("Debe ingresar un número positivo.")
    num = int(input("Intentelo de nuevo: "))

for i in range (num,-1,-1):
    suma += i

print (f"El resultado de la suma desde {num} hasta el 0 es {suma}")

#### **Ejercicio 8**

# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad = 0
num = 0
par = 0
impar = 0
negativos = 0
positivos = 0

print("Por favor, ingrese 100 números enteros")

while cantidad < 5: #Se deja 5 a modo de ejemplo
    num = int(input("Ingrese un número: "))
    cantidad += 1

    if num % 2 == 0:
        par += 1
    else:
        impar +=1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"La cantidad de números positivos ingresados es: {positivos}")
print(f"La cantidad de números negativos ingresados es: {negativos}")
print(f"La cantidad de números pares ingresados es: {par}")
print(f"La cantidad de números impares ingresados es: {impar}")

#### **Ejercicio 9**

# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

cantidad = 5 # Se deja 5 a modo de ejempl
suma = 0

print("Por favor, ingrese 100 números enteros")

for i in range (cantidad):
    num = int(input("Ingrese un número: "))
    suma += num

media = suma / cantidad

print(f"La media de los números ingresados es: {media}")

#### **Ejercicio 10**

# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


num = int(input("Ingresa un número: "))
invertido = int(str(num)[::-1])
#str(numero) convierte el número a texto.
#[::-1] invierte la cadena.
#int(...) vuelve a convertirlo a número.
print (f"El número invertido es {invertido}")