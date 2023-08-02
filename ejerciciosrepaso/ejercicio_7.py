def maximo_minimo(lista):
    if not lista:
        return None, None

    maximo = minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    return maximo, minimo

# Ejemplo de uso
lista_numeros = [10, 5, 25, -3, 15]
maximo, minimo = maximo_minimo(lista_numeros)

print(f"El número más grande es: {maximo}")
print(f"El número más pequeño es: {minimo}")
