while True :
    x =int(input("entrez un nombre : "))
    if x >= 0 :
        break
if x == 0:
    print("la factorielle de 0 est 1 ")
else :
    fa= 1
    for i in range(2,x+1):
        fa= fa * i
    print("la factorielle de ",x," est : ",fa)