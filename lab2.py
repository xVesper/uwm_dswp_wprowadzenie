"""Zadanie 1"""
napisz = input("Podaj linię danych rozdzielonych separatorem: ")
sep_zrd = input("Podaj separator źródłowy: ")
sep_doc = input("Podaj separator docelowy: ")
txt = napisz.split(sep_zrd)
wynik = sep_doc.join(txt)
print("Nowa linia danych: ", wynik)

"""Zadanie 2"""
zm = input("Wpisz cos: ")
ok = len(zm)//2
prw = zm[:ok]
drg = zm[ok:]
print("Pierwsza część:", prw)
print("Druga część:", drg)
drg_znak = zm[::-2]
print("Co drugi znak od końca:", drg_znak)

"""Zdanie 3"""
zm = input("Wpisz cos: ")
print("title()", zm.title())
print("capitalize()", zm.capitalize())
print("zfill()", zm.zfill(20))
print("upper()", zm.upper())
print("count()", zm.count("a"))
print("center()", zm.center(20,"_"))

"""Zadanie 4"""
txt = input("Wpisz cos: ")
print(f"{txt} isdecimal: {txt.isdecimal()}")
print(f"{txt} isalpha: {txt.isalpha()}")
print(f"{txt} isascii: {txt.isascii()}")
print(f"{txt} isprintable: {txt.isprintable()}")
print(f"{txt} istitle: {txt.istitle()}")
print(f"{txt} isupper: {txt.isupper()}")

"""Zadanie 5"""
txt = "Tomek"
liczba = 5
f_liczba = 5.245768943
duza_liczba = 100000000
print(f"{txt:<20}")
print(f"{txt:>20}")
print(f"{txt:^20}")
print(f"{liczba:05}")
print(f"{f_liczba:.2f}")
print(f"{duza_liczba:,}")

"""Zadanie 6"""
znaczki = [
   ("Alpha", "U+03B1"),
   ("Beta", "U+03B2"),
   ("Gamma", "U+03B3"),
   ("Delta", "U+03B4"),
   ("Epsilon", "U+03B5"),
   ("Zeta", "U+03B6"),
   ("Eta", "U+03B7"),
   ("Theta", "U+03B8"),
   ("Iota", "U+03B9"),
   ("Kappa", "U+03BA"),
   ("Pound", "U+00A3"),
   ("Bitcoin", "U+20BF"),
]
for znak, kod in znaczki:
    zmien = kod.replace("U+", "")
    print(f"{znak}: {kod} - {chr(int(zmien, 16))}")