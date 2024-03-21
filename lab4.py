"""Zadanie 1"""
for zm in range(0,51,5):
    print(zm)

"""Zadanie 2
Gorna czesc wzrasta od jednego o do pelnej szerokosci
Dolna czesc maleje z powrotem do jednego o
"""
zm1 = input("Podaj wysokosc: ")
help = int(zm1)
if (3 <= help <= 9) and (help%2==1):
    for i in range(1,help+1, 2): #gorna czesc tutaj o w kazdym wierszu
        for j in range((help - i) // 2): #tworzy spacje gdzie maleja te spacje w kazdym wierszu
            print(end=" ")
        for k in range(i): #drukuje o w wierszu czyli z kazdym i rosnie o
            print("o", end="")
        print()
    for i in range(help-2,0,-2): #dolna czesc tutaj o maleje bo juz zostala wykorzystana najwieksza czesc
        for j in range((help - i) // 2): #tworzy spacje ale tutaj rosnie nie maleje w kazdym wierszu
            print(end=" ")
        for k in range(i): #drukuje o w kazdym wierszu ale maleje o z kazdym wierszem
            print("o", end="")
        print()

"""Zadanie 3"""
print("    ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()
print("    " + "----" * 10)
for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()

"""Zadanie 4"""
txt = int(input("Podaj liczbe: "))
print(f"Binarnie -> {bin(txt)[2:]}\nÓsemkowo -> {oct(txt)[2:]}\nSzesnastkowo -> {hex(txt)[2:]}")

"""Zadanie 5"""
print("Wpisz q zeby zakonczyc petle\n")
while True:
    txt = input()
    if txt.lower()== 'q':
        break
    try:
        j = float(txt)
        print(f"{j} jest rzutowalna na float")
    except ValueError:
        print(f"{txt} nie jest rzutowalna na float")

    try:
        i = int(txt)
        print(f"{i} jest rzutowalna na int")
    except ValueError:
        print(f"{txt} nie jest rzutowalna na int")

"""Zadanie 6"""
import sys
sys.stdout.write("Podaj wartość liczbową: ")
txt = sys.stdin.readline().strip()
dlg = len(txt)
tab = []
for i, znak in enumerate(txt):
    dziesiatki = dlg - i - 1
    if znak != '0':
        tab.append(f"{10 ** dziesiatki} * {znak}")

wynik = " + ".join(tab)
sys.stdout.write(f"Podaną liczbę można zapisać jako: {wynik}\n")

"""Zadanie 7"""
import this
d = this.d
def kodowanie(txt):
    return ''.join([d.get(c, c) for c in txt])

print("Wpisz zdanie do zakodowania: ")
txt = input()
wynik = kodowanie(txt)
print(f"Zakodowane zdanie: {wynik}")

"""Zadanie 8"""
txt = input("Wpisz cos: ")
rozdziel = txt.split()
sortuj = sorted(txt, key=len)
print("Posortowane rosnąco: ")
print(' '.join(sortuj))

"""Zadanie 9"""
import random
poczatek = ["Szanowni Państwo,", "Wysoko Szanowni Państwo,", "Najdrożsi Zgromadzeni,", "Drodzy Obecni,", "Wszyscy Zgromadzeni,"]
srodek = ["pragnę zwrócić uwagę na", "należy podkreślić kwestię", "nie możemy zapominać o", "musimy pamiętać o", "powinniśmy rozważyć"]
koniec = ["zachowania równowagi społecznej.", "wzajemnego szacunku i zrozumienia.", "budowania wspólnego dobra.", "podtrzymywania tradycji i wartości.", "ciągłego rozwoju i dążenia do doskonałości."]
def generuj_zdania(n):
    for _ in range(n):
        yield random.choice(poczatek) + " " + random.choice(srodek) + " " + random.choice(koniec)

liczba_zdan = int(input("Podaj liczbe zdan do wygenerowania: "))
for zdanie in generuj_zdania(liczba_zdan):
            print(zdanie)