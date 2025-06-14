# Programación

## Práctico 11: Aplicación de la Recursividad 

### Ejercicio 1

# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario"


# Deficinición de funciones

def factorial(num):
  if num == 0:
    return 1
  else:
    return num* factorial (num-1)       
  
 #Programa principal

num= int(input("Ingrese un número: "))

for i in range(1,num+1):      
  print(f"El factorial de {i} es {factorial(i)}")


## Ejercicio 2

# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique.   
def fibonacci(n):
    if n == 0 or n == 1:   
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"El valor de la serie de Fibonaci en la posición 7 es: {fibonacci(7)}") # Tener el cuenta que el valor posicional contempla el 0

n = int(input("Indique hasta que posición quiere consultar la seria de Finoacci: "))
for i in range(n):
    print(f"El valor de la serie de Fibonaci en la posición {i} es: {fibonacci(i)}")


### Ejercicio 3

# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛(𝑚−1) #
#Prueba esta función en un algoritmo general.

def potencia(x,y):
    if y == 0:
        return 1
    else:
        return x * potencia(x, y - 1)

base = int(input("Ingrese el número del cuál desea saber el exponente: "))  
exponente = int(input("Ingrese exponente: "))  
print(f"{base} elevado a {exponente} es: {potencia(base, exponente)}")


#### Ejercicio 4

# Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_binario(num):
   if num == 0:
      return ""
   else:
      return decimal_binario(num//2) + str(num%2)
   
num = 10
print (f"{num} en binario es {decimal_binario(num)}")


##### Ejercicio 5

# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda;

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1])  # CORREGIDO

print(f"¿La palabra 'hoyessabado' es un palíndromo? {es_palindromo('hoyessabado')}")   
print(f"¿La palabra 'arrozalazorra' es un palíndromo? {es_palindromo('arrozalazorra')}")


###### Ejercicio 6

# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:No se puede convertir el número a string.//Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)


numero = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

####### Ejericio 7

# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca nbloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

n = int(input("Ingrese la cantidad de bloques en la base de su piramide: "))
print(f"La cantidad de bloques necesarios para construir su piramide son: {contar_bloques(n)}")


######## Ejercicio 8

# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
  if numero == 0:
    return 0
  elif numero % 10 == digito:
    return 1 + contar_digito(numero // 10, digito)
  else:
    return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito entre 0 y 9: "))
print(f"El {digito} aparece {contar_digito(numero,digito)} veces.")

