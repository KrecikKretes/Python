x=int(input("Podaj liczbe"))
k=0
if(x>2):
    for i in range (2, x-1):
        if(x%i==0):
            print("Liczba nie jest pierwsza")
            k=1
            break
else:
    if(x==2):
        print("Liczba jest pierwsza")
    print("Liczba nie jest pierwsza")
if(k==0):
    print("Liczba jest pierwsza")