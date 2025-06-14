def ingresar_dnis():
    cantidad = int(input("¿Cuántos DNIs desea ingresar? "))
    dnis = []
    for i in range(cantidad):
        dni = input(f"Ingrese el DNI #{i + 1} (solo números): ")
        while not dni.isdigit():
            dni = input("Entrada inválida. Ingrese solo números: ")
        dnis.append(dni)
    return dnis

def obtener_conjunto_digitos(dni):
    return set(dni)

def operaciones_conjuntos(conjuntos):
    union = set.union(*conjuntos)
    interseccion = set.intersection(*conjuntos)
    diferencias = [conjuntos[0].difference(c) for c in conjuntos[1:]]
    diferencia_simetrica = set.symmetric_difference(*conjuntos)
    return union, interseccion, diferencias, diferencia_simetrica

def contar_frecuencias(dni):
    frecuencia = {str(i): 0 for i in range(10)}
    for digito in dni:
        frecuencia[digito] += 1
    return frecuencia

def suma_digitos(dni):
    return sum(int(d) for d in dni)

def evaluar_condiciones(conjuntos):
    interseccion = set.intersection(*conjuntos)
    if interseccion:
        print("Dígito compartido:", interseccion)
    for i, conjunto in enumerate(conjuntos):
        if len(conjunto) > 6:
            print(f"DNI #{i+1}: Diversidad numérica alta")

# Programa principal
dnis = ingresar_dnis()
conjuntos = [obtener_conjunto_digitos(dni) for dni in dnis]

print("\n--- Operaciones con Conjuntos de Dígitos ---")
union, interseccion, diferencias, diferencia_simetrica = operaciones_conjuntos(conjuntos)
print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
for idx, diff in enumerate(diferencias, start=1):
    print(f"Diferencia del DNI #1 con el DNI #{idx+1}: {diff}")
print(f"Diferencia simétrica: {diferencia_simetrica}")

print("\n--- Frecuencia de Dígitos por DNI ---")
for idx, dni in enumerate(dnis):
    frec = contar_frecuencias(dni)
    print(f"DNI #{idx+1} ({dni}): {frec}")

print("\n--- Suma de Dígitos por DNI ---")
for idx, dni in enumerate(dnis):
    suma = suma_digitos(dni)
    print(f"DNI #{idx+1} ({dni}): Suma = {suma}")

print("\n--- Evaluación de Condiciones Lógicas ---")
evaluar_condiciones(conjuntos)