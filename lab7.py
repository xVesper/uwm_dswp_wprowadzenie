# -*- coding: utf-8 -*-
import csv
import datetime
'''Zadanie 1'''
# def extract_numbers(vals):
#     return [v for v in vals if isinstance(v, (int, float))]
#
# example_vals = [1, 'a', 2.5, (1, 2), 3, 'ok', 4.5, 'not', 100]
# extracted_numbers = extract_numbers(example_vals)
# print(extracted_numbers)
#
# '''Zadanie 2'''
# input_words = input("Wpisz cos: ")
# words_list = input_words.split()
# sorted_words = sorted(words_list, key=lambda word: len(word), reverse=True)
# print("Posortowane słowa DESC:", sorted_words)

'''Zadanie 3'''
# def sort_int_str(lst, reversed=False):
#     numbers = [item for item in lst if isinstance(item, int)]
#     strings = [item for item in lst if isinstance(item, str)]
#
#     sorted_numbers = sorted(numbers)
#     sorted_strings = sorted(strings)
#
#     if reversed:
#         return sorted_strings + sorted_numbers
#     else:
#         return sorted_numbers + sorted_strings
#
# example_list = ['apple', 1, 'banana', 10, 5, 'orange', 2]
# print(sort_int_str(example_list))
# print(sort_int_str(example_list, True))

'''Zadanie 4'''
# def clean_utarg(utarg):
#     utarg = utarg.replace('z', '').replace(',', '.').replace(' ', '')
#     return float(utarg) if utarg else 0
#
# def parse_date(date_str):
#     try:
#         return datetime.datetime.strptime(date_str, '%d.%m.%Y').strftime('%Y-%m-%d')
#     except ValueError:
#         return None
#
# def process_row(row):
#     if len(row) < 5:
#         print(f"Pomijam wiersz nie ma wystarczająco kolumn {row}")
#         return None
#     utarg = clean_utarg(row[4])
#     date = parse_date(row[2])
#     if date is None:
#         return None
#     return [row[0], date, row[1], utarg]
#
# def filter_country(rows, country):
#     return [row for row in rows if row[0] == country]
#
# with open('zamowienia.csv', 'r', encoding='utf-8', errors='ignore') as infile:
#     reader = csv.reader(infile, delimiter=';')
#     next(reader)
#     processed_rows = list(map(process_row, reader))
#     processed_rows = [row for row in processed_rows if row is not None]
#
# with open('zamowienia_polska.csv', 'w', newline='', encoding='utf-8') as outfile_pl:
#     writer_pl = csv.writer(outfile_pl)
#     polish_rows = filter_country(processed_rows, 'Polska')
#     writer_pl.writerows(polish_rows)
#
# with open('zamowienia_niemcy.csv', 'w', newline='', encoding='utf-8') as outfile_de:
#     writer_de = csv.writer(outfile_de)
#     german_rows = filter_country(processed_rows, 'Niemcy')
#     writer_de.writerows(german_rows)

'''Zadanie 5'''
def sort_dict_by_function(data_dict, func):
    if not callable(func):
        raise ValueError("Provided function is not callable")

    sorted_items = sorted(data_dict.items(), key=lambda item: func(item[1]))
    return sorted_items

example_dict = {
    'Jan': [1, 3, 4, 7],
    'Anna': [2, 3, 5, 10],
    'Ewa': [-1, -2, -3, -4],
    'Piotr': [1, -1, 2, -2]
}

sorted_by_min = sort_dict_by_function(example_dict, min)
sorted_by_max = sort_dict_by_function(example_dict, max)
sorted_by_sum = sort_dict_by_function(example_dict, sum)

print("Posortowane funkcja min:", sorted_by_min)
print("Posortowane funkcja max:", sorted_by_max)
print("Posortowane funkcja sum:", sorted_by_sum)




