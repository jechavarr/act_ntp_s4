# Función que recibe una lista de números y devuelve una nueva lista con solo los números pares
def obtener_numeros_pares(lista_numeros):
    # Creamos una lista vacía para almacenar los números pares
    numeros_pares = []

    # Recorremos la lista original usando un ciclo for
    for numero in lista_numeros:
        # Verificamos si el número es par (divisible entre 2)
        if numero % 2 == 0:
            numeros_pares.append(numero)  # Lo agregamos a la nueva lista

    # Devolvemos la lista con los números pares
    return numeros_pares

# Lista de prueba
lista_prueba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Llamamos a la función con la lista de prueba y mostramos el resultado
resultado = obtener_numeros_pares(lista_prueba)
print("Números pares:", resultado)