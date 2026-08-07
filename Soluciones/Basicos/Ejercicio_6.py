# Escribe el código aquí
par = 0 #suma de pares
impar = 0 #Suma de impares

numer = input()
lista_number = list(numer)

for i in range(len(numer)):
    n = int(lista_number[i])
    if n%2==0:
        par+=n
    else:
        impar+=n

print(f"Sum even: {par}")
print(f"Sum odd: {impar}")


