'''Zadanie 1'''
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prw_piec = lists[:5]
ostatnie = lists[5:]
print(prw_piec)
print(ostatnie)

'''Zadanie 2'''
nowa_lista = [prw_piec[:5], ostatnie]
nowa_lista[0].insert(0, 0)
sortowanie = nowa_lista[0] + nowa_lista[1]
cp_sortowanie = sortowanie.copy()
cp_sortowanie.sort(reverse=False)
print(cp_sortowanie)

'''Zadanie 3'''
txt = input("Wpisz cos: ")
male = ''.join(sorted(set(txt.lower())))
print(male)

'''Zadanie 4'''
msc = {
    1: "Styczeń",
    2: "Luty",
    3: "Marzec",
    4: "Kwiecień",
    5: "Maj",
    6: "Czerwiec",
    7: "Lipiec",
    8: "Sierpień",
    9: "Wrzesień",
    10: "Październik",
    11: "Listopad",
    12: "Grudzień"
}
for dzien, miesiac in msc.items():
    print(f"{dzien}: {miesiac}")

'''Zadanie 5'''
msc = {
    1: "Styczeń",
    2: "Luty",
    3: "Marzec",
    4: "Kwiecień",
    5: "Maj",
    6: "Czerwiec",
    7: "Lipiec",
    8: "Sierpień",
    9: "Wrzesień",
    10: "Październik",
    11: "Listopad",
    12: "Grudzień"
}
msc_eng = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

miesiace = {'pl': msc, 'en': msc_eng}

print(miesiace['pl'][4])
print(miesiace['en'][4])

'''
Zadanie 6
Tak można używać dynamicznie, przekazując do tej funkcji argumentu value, który będzie wspólną wartością dla wszystkich kluczy.
'''
imie = 'Marianna'
slownik = dict.fromkeys(imie,1)
print(slownik)

'''Zadanie 7'''
import string
tekst = input("Wpisz coś: ")
ilosc_alfabetu = sum(1 for txt in tekst if txt.islower() and txt in string.ascii_lowercase)
ilosc_cyfr = sum(1 for txt in tekst if txt in string.digits)
print(f"Ilość znaków: {ilosc_alfabetu}")
print(f"Ilość cyfr: {ilosc_cyfr}")