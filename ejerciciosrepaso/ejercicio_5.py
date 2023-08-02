def conversion(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5 / 9
    return grados_celsius


grados_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
grados_celsius = conversion(grados_fahrenheit)
print(f"{grados_fahrenheit:.2f} °F equivale a {grados_celsius:.2f} °C.")
