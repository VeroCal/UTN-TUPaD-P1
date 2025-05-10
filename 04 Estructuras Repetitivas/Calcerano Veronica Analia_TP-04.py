# **Ejercicio 1**
# Simulación de Puertas Lógicas Básicas:
# Programa en Python que simule las puertas AND, OR y NOT. Soliciten al usuario ingresar valores binarios (0 o 1) y muestren el resultado de cada operación.
# Extensión: Agregar puertas adicionales (NAND, NOR, XOR) si lo desean.

binario_1 = int(input("Ingresa un número binario (1 o 0): "))
binario_2 = int(input("Ingresa otro número binario: "))

while not (binario_1 in [0,1] and binario_2 in [0,1]):
  print("Uno de los números ingresados no es correcto. Recuerde que los números binarios pueden ser solo 1 o 0.") 
  binario_1 = int(input("Ingresa un número binario: "))
  binario_2 = int(input("Ingresa otro número binario: "))
else: 
    print("A\tB\tAND\tOR\tXOR\tNOT A\tNOT B\tNAND")
    print("-" * 65) #linea divisoria
    print(f"{binario_1}\t{binario_2}\t{binario_1 & binario_2}\t{binario_1| binario_2}\t{binario_1 ^ binario_2}\t{int(not binario_1)}\t{int(not binario_2)}\t{int(not (binario_1 & binario_2))}")

otro_numero = input("Desea agregar un tercer número binario? (s/n): ").lower()
if otro_numero == "s": # type: ignore
    binario_3 = int (input("Ingresa otro número binario: "))
    while not (binario_3 in [0,1]):
        print("El número ingresado no es correcto. Recuerde que los números binarios pueden ser solo 1 o 0.") 
        binario_3 = int (input("Ingresa un número binario: "))
    #no es necesario el uso de ELSE 
    print("A\tB\tC\tAND\tOR\tXOR\tNOT A\tNOT B\tNOT C\tNAND")
    print("-" * 80) #linea divisoria
    print(f"{binario_1}\t{binario_2}\t{binario_3}\t{binario_1 & binario_2 & binario_3}\t{binario_1| binario_2| binario_3}\t{binario_1 ^ binario_2 ^ binario_3}\t{int(not binario_1)}\t{int(not binario_2)}\t{int(not binario_3)}\t{int(not (binario_1 & binario_2 & binario_3))}")
    print("Ha finalizado el proceso")
elif otro_numero == "n":
    print("Ha finalizado el proceso")
elif otro_numero != "n" or otro_numero != "s":
    print ("La información ingresada no es válida. Ha finalizado el proceso")
    

#Conversión de Números:
#Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
#Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.    

numero_decimal = int(input("Ingrese un número decimal: "))
binario = bin(numero_decimal)[2:] 
print(f"El número {numero_decimal} en binario es {binario}")
otro_decimal = input("Desea convertir otro número en binario? (s/n): ").lower()

while otro_decimal not in ["s", "n"]:
        print("El dato ingresado no es válido.")
        otro_decimal = input("Ingrese ""S"" para convertir otro número o ""N"" para continuar: ").lower()

while otro_decimal == "s":
    numero_decimal = int(input("Ingrese otro número decimal: "))
    binario = bin(numero_decimal)[2:] 
    print(f"El número {numero_decimal} en binario es {binario}")
    otro_decimal = input("Desea convertir otro número en binario? (s/n): ").lower()

    while otro_decimal not in ["s", "n"]:
        print("El dato ingresado no es válido.")
        otro_decimal = input("Desea convertir otro número en binario? (s/n): ").lower()

if otro_decimal == "n":
    convierte_binario = input("Quiere convertir un número binario en decimal? (s/n): ").lower()
    
    while convierte_binario not in ["s", "n"]:
        print("El dato ingresado no es válido.")
        convierte_binario = input("Ingrese ""S"" para convertir otro número o ""N"" para finalizar: ").lower()

    while convierte_binario == "s":
        numero_binario = input("Ingrese un número binario: ")
        decimal = int(numero_binario, 2)
        print(f"El número {numero_binario} en decimal es {decimal}")
        convierte_binario = input("Desea convertir otro número en decimal? (s/n): ").lower()
        
        while convierte_binario not in ["s", "n"]:
          print("El dato ingresado no es válido.")
          convierte_binario = input("Ingrese ""S"" para convertir otro número o ""N"" para finalizar: ").lower()
        
    print ("El proceso ha finalizado.")



        