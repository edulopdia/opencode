Cantidad = int(input("Porfavor dame la cantidad de números que usaremos "))

numeros = []

for i in range(Cantidad):
    numero = int(input(f"Dame un número {i + 1}: "))
    numeros.append(numero)

print("Los números guardados son:", numeros)


print("El número menor es:", min(numeros))
print("El número mayor es:", max(numeros))


Rango1 = int(input("Introduce el primer número del rango: "))
Rango2 = int(input("Introduce el segundo número del rango: "))

inicio = min(Rango1, Rango2)
fin = max(Rango1, Rango2)

lista_rango = []
for numero in numeros:
    if inicio <= numero <= fin:
        lista_rango.append(numero)

print(f"Números entre {inicio} y {fin}:", lista_rango)