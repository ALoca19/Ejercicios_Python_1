#H: altura del vecindario
#W: ancho del vecindario
H, W = [int(x) for x in input().split()]

vecindario = []
for _ in range(H):
    fila = [0]*W
    vecindario.append(fila)


#Numero de casas que DEBEN estar pintadas en gris
N= int(input())

#Casas pintadas en gris
M=int(input())

#Coordenadas de las casas pintadas

for _ in range(M):
    x1, y1 = [int(x) for x in input().split()]
  
    vecindario[x1-1][y1-1]=1

#Caluclamos las casas pintadas
casas_expadir = []
for r in range(H):
    for c in range(W):
        if vecindario[r][c]==1:
            casas_expadir.append((r,c))

meses = 0
total = M

while total<N:

    nuevas_pintadas = []
    
    meses+=1

    for x, y in casas_expadir:
        X, Y = x+1, y 
        if 0 <= X < H and 0<= Y < W and vecindario[X][Y] == 0:
            vecindario[X][Y]=1
            total+=1
            nuevas_pintadas.append((X, Y))

        X, Y = x-1, y 
        if 0 <= X < H and 0<= Y < W and vecindario[X][Y] == 0:
            vecindario[X][Y]=1
            total+=1
            nuevas_pintadas.append((X, Y))

        X, Y = x, y+1 
        if 0 <= X < H and 0<= Y < W and vecindario[X][Y] == 0:
            vecindario[X][Y]=1
            total+=1
            nuevas_pintadas.append((X, Y))

        X, Y = x, y-1 
        if 0 <= X < H and 0<= Y < W and vecindario[X][Y] == 0:
            vecindario[X][Y]=1
            total+=1
            nuevas_pintadas.append((X, Y))

    casas_expadir = nuevas_pintadas

print(meses)