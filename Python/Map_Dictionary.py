Dict = {"dom":"house","butelka":"bootle"}
x=input("Podaj wyraz\n")
print(Dict[x])

slownik = {"muzyka": "music", "język": "language", "symulacja": "simulation"}

print("Możliwe opcje do tłumaczenia:")
for key in slownik.keys():
    print(key, end=", ")
print("\n")
polskieSlowo = input("Wpisz tekst \n").lower()

if polskieSlowo in slownik:
    print("Przetłumaczony wyraz:",slownik[polskieSlowo])
else:
    print("Podałeś slowo poza słownika")
