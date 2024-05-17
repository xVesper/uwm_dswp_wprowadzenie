# -*- coding: utf-8 -*-
'''Zadanie1'''
from timeit import timeit
import random
import string
setup = """
from array import array
import random
import string
"""
stmt_char_array = """
tab_of_chars = array('u', [random.choice(string.ascii_letters) for _ in range(1_000_000)])
"""
stmt_char_list = """
list_of_chars = [random.choice(string.ascii_letters) for _ in range(1_000_000)]
"""

stmt_int_array = """
tab_of_ints = array('i', [random.randint(0, 100) for _ in range(1_000_000)])
"""
stmt_int_list = """
list_of_ints = [random.randint(0, 100) for _ in range(1_000_000)]
"""

stmt_long_array = """
tab_of_longs = array('l', [random.randint(0, 100) for _ in range(1_000_000)])
"""
stmt_long_list = """
list_of_longs = [random.randint(0, 100) for _ in range(1_000_000)]
"""

print("Czas inicjalizacji tablicy znaków: ", timeit(stmt_char_array, setup, number=100))
print("Czas inicjalizacji listy znaków: ", timeit(stmt_char_list, setup, number=100))

print("Czas inicjalizacji tablicy liczb całkowitych: ", timeit(stmt_int_array, setup, number=100))
print("Czas inicjalizacji listy liczb całkowitych: ", timeit(stmt_int_list, setup, number=100))

print("Długi czas inicjalizacji tablicy liczb całkowitych: ", timeit(stmt_long_array, setup, number=100))
print("Długi czas inicjalizacji listy liczb całkowitych: ", timeit(stmt_long_list, setup, number=100))

'''Zadanie2'''
from array import array
import random
from datetime import datetime

tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])
list_of_floats = [random.random() for _ in range(1_000_000)]

start_time = datetime.now()
with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)
write_time_array = datetime.now() - start_time

start_time = datetime.now()
tab_of_floats_loaded = array('f')
with open('floats_array.bin', 'rb') as file_arr:
    tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
read_time_array = datetime.now() - start_time

start_time = datetime.now()
with open('floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))
write_time_list = datetime.now() - start_time

start_time = datetime.now()
with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()
list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
read_time_list = datetime.now() - start_time

print(f"Czas zapisu tablicy: {write_time_array.total_seconds()}s")
print(f"Czas odczytu tablicy: {read_time_array.total_seconds()}s")
print(f"Czas zapisu listy: {write_time_list.total_seconds()}s")
print(f"Czas odczytu listy: {read_time_list.total_seconds()}s")

'''Zadanie3'''
from collections import deque
from datetime import datetime

num_operations = 1_000_000

deque_obj = deque()
start_time = datetime.now()
for _ in range(num_operations):
    deque_obj.append(0)
time_deque_append = datetime.now() - start_time

deque_obj = deque()
start_time = datetime.now()
for _ in range(num_operations):
    deque_obj.appendleft(0)
time_deque_appendleft = datetime.now() - start_time

list_obj = []
start_time = datetime.now()
for _ in range(num_operations):
    list_obj.append(0)
time_list_append = datetime.now() - start_time
list_obj = []
start_time = datetime.now()
for _ in range(num_operations):
    list_obj.insert(0, 0)
time_list_insert = datetime.now() - start_time

print(f"Deque append czas: {time_deque_append.total_seconds()}s")
print(f"Deque appendleft czas: {time_deque_appendleft.total_seconds()}s")
print(f"List append czas: {time_list_append.total_seconds()}s")
print(f"List insert(0, ...) czas: {time_list_insert.total_seconds()}s")

'''Zadanie4'''
import csv
from collections import namedtuple
def sanitize_fieldnames(fieldnames):
    return [field.replace(' ', '_').replace('-', '_') for field in fieldnames]
with open('zamowienia.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    headers = next(reader)
    sanitized_headers = sanitize_fieldnames(headers)
    Order = namedtuple('Order', sanitized_headers)
    orders = [Order(*row) for row in reader]
for order in orders[:5]:
    print(order)

'''Zadanie5'''
import random
def top_10_percent(values):
    if not values:
        return []
    sorted_values = sorted(values, reverse=True)
    top_n = max(1, len(sorted_values) // 10)
    return sorted_values[:top_n]
values = [random.randint(1, 100) for _ in range(100)]
top_values = top_10_percent(values)
print("10% wartości:", top_values)

'''Zadanie6'''
from collections import Counter, deque
def create_kolo_fortuny(*args):
    counter = Counter(args)
    kolo_fortuny_deque = deque(counter.elements())
    return kolo_fortuny_deque
kolo_fortuny = create_kolo_fortuny('apple', 'banana', 'apple', 'orange', 'banana', 'apple')
print(kolo_fortuny)

'''Zadanie7'''
from collections import Counter, deque
import time
import numpy as np

def create_kolo_fortuny(*args):
    counter = Counter(args)
    kolo_fortuny_deque = deque(counter.elements())

    return kolo_fortuny_deque


def spinit(ticks: int):
    waits = np.logspace(0.0, 1.0, num=ticks) / ticks

    for tick in range(ticks):
        print(f'{tick}', end='')
        time.sleep(waits[tick])
        print('\r', end='')


def rotate_and_display(kolo_fortuny, rotations):
    for _ in range(rotations):
        kolo_fortuny.rotate(1)
        print(f'Aktualnie: {list(kolo_fortuny)}')
        time.sleep(0.2)

    print(f'Zatrzymano na: {kolo_fortuny[0]}')

kolo_fortuny = create_kolo_fortuny('apple', 'banana', 'apple', 'orange', 'banana', 'apple')
print("Inizjalizowanie:", list(kolo_fortuny))

rotate_and_display(kolo_fortuny, 10)
