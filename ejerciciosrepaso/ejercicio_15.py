cadena = input("Ingrese una cadena de texto: ")
cadena = cadena.lower()
cadena = cadena.replace(" ", "")
inversa = cadena[::-1]

if cadena == inversa:
    print(f"La cadena '{cadena}' es un palíndromo")
else:
    print(f"La cadena '{cadena}' no es un palíndromo")
