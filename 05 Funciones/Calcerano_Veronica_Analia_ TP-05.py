#Ejercicio 1

# Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Definición de funciones
def imprimir_hola_mundo ():
  return "Hola mundo!"

# Programa principal
print(imprimir_hola_mundo())

# Ejercicio 2

# Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función


# Definición de funciones
def saluda_usuario(nombre):
  return "Hola " + nombre + "!"

# Programa principal
print(saluda_usuario("Marcos"))



# Ejercicio 3

# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definición de funciones
def informacion_personal(nombre,apellido,edad,residencia):
  return (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
print(informacion_personal(nombre,apellido,edad,residencia))

#Ejercicio 4

#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Defenición de funciones

def calcular_area_circulo(radio):
  area = 3.14 * radio ** 2
  return area

def  calcular_perimetro_circulo(radio):
  perimetro = 2 * 3.14 * radio
  return perimetro


# Programa principal

radio = float (input("Ingrese el radio: "))
print(f"El área del circulo es de: {calcular_area_circulo(radio)}")
print(f"El perímetro del circulo es de: {calcular_perimetro_circulo(radio)}")

#Ejercicio 5

#Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Definición de funciones

def segundos_a_horas(segundos):
  horas = segundos / 3600
  return horas

# Programa principal

segundos = int(input("Ingrese los segundos: "))
print(f"{segundos} segundos, son {segundos_a_horas(segundos)} horas")

# Ejercicios 6

# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definición de funciones

def tabla_multiplicar(numero):
  for i in range(1,11):
    resultado = numero * i
    print (f"{numero} x {i} = {resultado}")   # En este caso no fue necesario el return, ya que sino traía de nuevo el resultado final


# Programa principal

numero = int(input("Ingresa un número: "))
tabla_multiplicar(numero)

# Ejercicio 7

# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Definición de funciones

def operaciones_basicas(a,b):
  print(f"{a} + {b} = {a+b}")
  print(f"{a} - {b} = {a-b}")
  print(f"{a} * {b} = {a*b}")
  print(f"{a} / {b} = {a//b}")

# Programa principal
a = int(input("Ingresa un número entero: "))
b = int(input("Ingresa otr número entero: "))

operaciones_basicas(a,b)

# Ejercicio 8

# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Definición de funciones

def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  imc = round(imc, 2)
  return imc


# Programa principal
peso = int(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

print(f"Su IMC es: {calcular_imc(peso,altura)} ")

# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Definición de funciones

def celsius_a_fahrenheit(celsius):
  fahrenheit = celsius * 9/5 + 32
  return fahrenheit

 # Programa principal

celsius = float(input("Inagrese los grados Celsius: "))
print(f"{celsius} grados Celsius, son {celsius_a_fahrenheit(celsius)} grados Fahrenheit")

# Ejercicio 10

# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# Definicion de funciones

def calcular_promedio(a,b,c):
  promedio = (a+b+c) / 3
  return promedio

# Programa principal
a = int(input("Ingrese la primer nota: "))
b = int(input("Ingrese la segunda nota: "))
c = int(input("Ingrese la tercer nota: "))

print(f"El promedio de las tres notas es: {calcular_promedio(a,b,c)}")