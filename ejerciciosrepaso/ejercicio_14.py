def media_aritmetica(lista):
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")

    suma = sum(lista)
    cantidad = len(lista)
    cantidad_media = suma / cantidad
    return cantidad_media

numeros = [10, 20, 30, 40, 50]
resultado = media_aritmetica(numeros)
print(f"La media aritmética de {numeros} es {resultado}")
