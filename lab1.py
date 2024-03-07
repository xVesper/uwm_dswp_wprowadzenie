'''Zadanie 1'''
zmienna1 = int(5)
zmienna2 = int(2)
zmienna3 = float(20.8)
zmienna4 = float(1.3)
print(f"Wartość int: {zmienna1} oraz {zmienna2}"
      f"\n Wartość float {zmienna3} oraz {zmienna4}")

'''Zadanie 2'''
zmienna = int(5)
zmienna2 = float(2.2)
wynik = zmienna.bit_count() if hasattr(zmienna, 'bit_count') else "Metoda bit_count niedostępna"
print(f"Wartość {zmienna} to {wynik}")
print("Fałsz: ", zmienna2.is_integer())
print("Prawda: ", float(2).is_integer())  # float(2) zamiast float.is_integer(2), bo metoda dotyczy instancji

'''Zadanie 3'''
binarnie = bin(10)[2:]  # Usunięcie prefiksu "0b"
calkowicie = int(binarnie, base=2)
print(f"Liczba całkowita {calkowicie} na ciąg binarny to {binarnie}")

'''Zadanie 4 '''
x = int(5)
y = int(2)
print(f"Alternatywa rozłączna: {x | y} \n"  # Zmiana ^ na |
      f"Koniunkcja: {x & y} \n"  # Zmiana & na |
      f"Przesunięte w lewo o n bitów: {x << y} \n"
      f"Przesunięte w prawo o n bitów: {x >> y} \n"
      f"Negacja x: {~x} \n"
      f"Negacja y: {~y} \n")

'''Zadanie 5'''
przecinek = float(2.2)
szesnastkowa = float.hex(przecinek)
print(f"Wartość {przecinek} szesnastkowo {szesnastkowa}")
powrot = float.fromhex(szesnastkowa)
print(f"Wartość {szesnastkowa} zmiennoprzecinkowo {powrot}")