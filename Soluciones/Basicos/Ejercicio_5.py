
edad_perro = int(input())
edad_humana = 0
i=0
    
while i<edad_perro:
    i+=1
    if i==1:
        edad_humana+=15
    elif i==2:
        edad_humana+=9
    elif 3<=i<=6:
        edad_humana+=4
    else:
        edad_humana+=5
        
print(edad_humana)