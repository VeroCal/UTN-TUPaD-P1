#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


edades = []
for i in range(3):
    edad = int(input("Ingresá la edad: "))
    i += 1 
    edades.append(edad)

priomedio = sum(edades)/len(edades)    

print("Las edades ingresadas son:", edades)
print("El promedio de las edades ingresadas es:", priomedio)