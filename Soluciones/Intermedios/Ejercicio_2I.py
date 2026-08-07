C, R = input().split()
N = int(input())
ataque = 0
col_c=ord(C)
fil_c=int(R)

for _ in range(N):
    piezas_oponente= input().split()
    col_o = ord(piezas_oponente[0])
    fil_o = int(piezas_oponente[1])

    dif_col=abs(col_c-col_o)
    dif_fil=abs(fil_c-fil_o)

    if (dif_col == 2 and dif_fil==1) or (dif_col == 1 and dif_fil == 2):
        ataque+=1

print(ataque)