import time
import random

#Algoritmo 1, suma los números 1 por 1, de manera iterativa. Realiza la sumatoria y el cálculo de la media

def media_iteracion(numeros):
    total=0
    for num in numeros:
        total+=num                   #Suma acumulativa
    return total/len(numeros)       # Se divide por la cantidad de elementos

#Algoritmo 2, utiliza la función sum para realizar la sumatoria y luego calcula la media.

def media_sum(numeros):             # sum() recorre la lista internamente
    return sum(numeros) / len(numeros)


#Función para medir el tiempo: mide el tiempo en milisegundos

def tiempo(funcion,numeros):      #Tiempo inicial
    start=time.time()
    resultado=funcion(numeros)    #Se ejecuta la función pasada como argumento
    end=time.time()
    return resultado, (end-start) * 1000 # Se devuelve el resultado y el tiempo en ms

#Programa Principal

def main():

#Pruebas

    print("n\t media_iteracion (ms)")
    for i in range(1, 9):            # Se prueban listas de tamaño 10^1 hasta 10^8
        cantidad = 10**i
        numeros = [random.randint(1, 100) for _ in range(cantidad)]     #Se genera una lista aleatoria 
        _, duracion = tiempo(media_iteracion, numeros)
        print(f"{cantidad}\t{duracion:.6f}")
       

    print("\nn\t media_sum (ms)")
    for i in range(1, 9):            #Se respetan los mismos tamaños para el segundo algoritmo
        cantidad = 10**i
        numeros = [random.randint(1, 100) for _ in range(cantidad)] #Se genera una lista aleatoria
        _, duracion = tiempo(media_sum, numeros)
        print(f"{cantidad}\t{duracion:.6f}")

if __name__ == "__main__":
    main()