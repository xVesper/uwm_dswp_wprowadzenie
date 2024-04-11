import csv
import datetime
import os
import unidecode
import random

'''Zadanie 1'''
with open('zamowienia.csv', 'r', encoding='utf-8', errors='ignore') as infile:
    reader = csv.reader(infile, delimiter=';')
    next(reader)
    rows = []
    for i, row in enumerate(reader, start=2):
        if len(row) < 5:
            print(f"Pomijam wiersz {i} nie ma wystarczająco kolumn {row}")
            continue

        utarg = row[4].replace('z', '')
        utarg = utarg.replace(',', '.')
        utarg = utarg.replace(' ', '')
        try:
            data = datetime.datetime.strptime(row[2], '%d.%m.%Y').strftime('%Y-%m-%d')
        except ValueError as e:
            print(f"Error processing date in row {i}: {e}")
            continue

        row = [row[0], data, row[1], utarg]
        rows.append(row)

    with open('zamowienia_polska.csv', 'w', newline='', encoding='utf-8') as outfile_pl:
        writer_pl = csv.writer(outfile_pl)
        writer_pl.writerows(row for row in rows if row[0] == 'Polska')

    with open('zamowienia_niemcy.csv', 'w', newline='', encoding='utf-8') as outfile_de:
        writer_de = csv.writer(outfile_de)
        writer_de.writerows(row for row in rows if row[0] == 'Niemcy')

'''Zadanie 2'''
def concatenate_files(file_list, output_file):
    with open(output_file, 'w') as outfile:
        for file in file_list:
            if os.path.isfile(file):
                with open(file, 'r') as infile:
                    outfile.write(infile.read())
            else:
                print(f"Error: Plik '{file}' nie istnieje")
file_list = ['file1.txt', 'file2.txt', 'file3.txt']
output_file = 'output.txt'
concatenate_files(file_list, output_file)

'''Zadanie 3'''
def n_largest_or_smallest(numbers, n=1, ascending=True):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Lista musi posiadać tylko liczby")
    sorted_numbers = sorted(numbers, reverse=not ascending)
    return sorted_numbers[:n]

numbers = [3, 5, 7, 2, 8, 1, 9, 6, 4]
print(n_largest_or_smallest(numbers, n=3))
print(n_largest_or_smallest(numbers, n=2, ascending=False))

'''Zadanie 4'''
def type_groups(mixed):
    type_dict = {}
    for element in mixed:
        element_type = type(element).__name__
        if element_type not in type_dict:
            type_dict[element_type] = []
        type_dict[element_type].append(element)
    return type_dict

mixed = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
type_dict = type_groups(mixed)
print(type_dict)

'''Zadanie 5'''
def split_surnames(surnames):
    file1_surnames = []
    file2_surnames = []
    for surname in surnames:
        surname = unidecode.unidecode(surname)
        if surname[0].lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']:
            file1_surnames.append(surname)
        else:
            file2_surnames.append(surname)
    with open('A-M_nazwiska.txt', 'w') as file1:
        for surname in file1_surnames:
            file1.write(surname + '\n')
    with open('N-Ż_nazwiska.txt', 'w') as file2:
        for surname in file2_surnames:
            file2.write(surname + '\n')

surnames = ['Kowalski', 'Nowak', 'Szewczyk', 'Wiśniewski', 'Zając']
split_surnames(surnames)

'''Zadanie 6'''
def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    reversed_text = ' '.join(reversed_words)
    print(reversed_text)

text = "Ala ma kota"
reverse_words(text)

'''Zadanie 7'''
def deal_cards():
    ranks = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Walet', 'Dama', 'Król']
    suits = ['pik', 'karo', 'trefl', 'kier']

    deck = [rank + ' ' + suit for rank in ranks for suit in suits]

    random.shuffle(deck)
    hands = [deck[i:i+5] for i in range(0, len(deck), 5)]
    for i, hand in enumerate(hands):
        print(f"Gracz {i+1}: {hand}")

deal_cards()

'''Zadanie 8'''
def generate_emails(filename, domain):
    with open(filename, 'r', encoding='utf-8') as f:
        names = f.readlines()

    with open('email_addresses.txt', 'w', encoding='utf-8') as f:
        for name in names:
            name = name.strip().replace(',', '')
            first_name, last_name = name.split()
            first_name = unidecode.unidecode(first_name).lower()
            last_name = unidecode.unidecode(last_name).lower()
            email = f"{first_name}.{last_name}@{domain}"
            f.write(f"{name}, {email}\n")

generate_emails('names.txt', 'student.uwm.edu.pl')

'''Zadanie 9'''
def load_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]


def play_game(words):
    word = random.choice(words).lower()
    guesses = []
    masked_word = ['_' if c != ' ' else ' ' for c in word]
    lives = 5
    print(' '.join(masked_word))
    print(f'Życia: {lives}')

    while True:
        guess = input('Wpisz literę lub całe hasło: ').strip().lower()
        if len(guess) > 1:
            if guess == word:
                print(f'Gratulacje! Zgadłeś słowo: {word}')
                break
            else:
                print('Niestety to nie jest poprawne hasło.')
                lives -= 1
        elif guess in guesses:
            print(f'Już odgadłeś literę: {guess}')
        elif guess in word:
            for i, c in enumerate(word):
                if c == guess:
                    masked_word[i] = guess
            print(' '.join(masked_word))
        else:
            print(f'Przepraszamy, w słowie nie ma litery: {guess}')
            lives -= 1

        guesses.append(guess)
        print(f'Życia: {lives}')

        if lives == 0:
            print(f'Koniec gry! Prawidłowe słowo to: {word}')
            break
        if '_' not in masked_word:
            print(f'Gratulacje! Zgadłeś całe hasło: {word}')
            break

words = load_words('words.txt')
play_game(words)


