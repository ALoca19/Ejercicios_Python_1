N = int(input())
contar_anagramas = 0

for _ in range(N):
    a, b = input().split()

    if sorted(a)==sorted(b):
        contar_anagramas+=1

print(contar_anagramas)