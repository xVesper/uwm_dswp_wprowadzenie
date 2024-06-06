# -*- coding: utf-8 -*-
import os
import pandas as pd
from zipfile import ZipFile
from datetime import datetime, timedelta
import pytz

'''Zadanie 1'''
def create_directories(paths):
    for path in paths:
        try:
            exist_ok=True
            os.makedirs(path, exist_ok=True)
            print(f"Folder '{path}' został utworzony lub już istnieje.")
        except Exception as e:
            print(f"Nie można utworzyć folderu '{path}': {e}")

paths = ["1", "2", "3"]
create_directories(paths)

'''Zadanie 2'''
def merge_txt_to_csv(zip_path, output_file):
    all_data = []
    headers = None

    with ZipFile(zip_path, 'r') as z:
        txt_files = [f for f in z.namelist() if f.endswith('.txt')]
        for file in txt_files:
            with z.open(file) as f:
                try:
                    data = pd.read_csv(f, delimiter="\t")

                    if headers is None:
                        headers = data.columns.tolist()
                        all_data.append(data)
                    else:
                        if list(data.columns) == headers:
                            all_data.append(data)
                except pd.errors.EmptyDataError:
                    print(f"Ostrzeżenie: Plik {file} jest pusty lub nie zawiera danych do odczytu.")
                except Exception as e:
                    print(f"Ostrzeżenie: Wystąpił błąd przy odczycie pliku {file}: {e}")

    if all_data:
        combined_data = pd.concat(all_data, ignore_index=True)
        combined_data.to_csv(output_file, index=False)
        print(f"Plik {output_file} został utworzony.")
    else:
        print("Nie znaleziono danych do scalenia.")

merge_txt_to_csv('data_for_lab_10.zip', 'wynikowy_plik.csv')


'''Zadanie 3'''
def convert_time(input_time, timezone):
    utc_time = datetime.strptime(input_time, "%H:%M:%S").replace(tzinfo=pytz.utc)
    target_time = utc_time.astimezone(pytz.timezone(timezone))
    return target_time.strftime("%H:%M:%S")
user_time = input("Podaj czas w formacie HH:MM:SS: ")

timezones = {
    "Tokyo": "Asia/Tokyo",
    "Washington": "America/New_York",
    "Sydney": "Australia/Sydney",
    "London": "Europe/London"
}

for city, zone in timezones.items():
    time_in_zone = convert_time(user_time, zone)
    print(f"Czas w {city}: {time_in_zone}")

'''Zadanie 4'''
def calculate_age_and_next_birthday(birthdate):
    today = datetime.today()
    next_birthday = datetime(today.year, birthdate.month, birthdate.day)

    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)

    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    last_birthday = datetime(
        today.year - 1 if (today.month, today.day) < (birthdate.month, birthdate.day) else today.year,
        birthdate.month, birthdate.day)
    days_since_last_birthday = (today - last_birthday).days
    months = days_since_last_birthday // 30
    days = days_since_last_birthday % 30

    days_to_next_birthday = (next_birthday - today).days

    print(f"Dzisiaj masz {age} lat, {months} miesięcy i {days} dni.")
    print(f"Do twoich kolejnych urodzin pozostało {days_to_next_birthday} dni.")

birthdate_input = input("Podaj datę urodzenia (format YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")
calculate_age_and_next_birthday(birthdate)

'''Zadanie 5'''
def convert_date_in_zip(zip_path, file_name, date_col_index, source_format, output_name):
    with ZipFile(zip_path) as z:
        with z.open(file_name) as file:
            df = pd.read_csv(file)

            df.iloc[:, date_col_index] = pd.to_datetime(df.iloc[:, date_col_index], format=source_format).dt.strftime(
                '%Y-%m-%d')

            output_path = os.path.join(os.path.dirname(zip_path), output_name)
            df.to_csv(output_path, index=False)

zip_path = 'data_for_lab_10.zip'
file_name = 'data.csv'
date_col_index = 0
source_format = '%d/%m/%Y'
output_name = 'converted_dates.csv'

convert_date_in_zip(zip_path, file_name, date_col_index, source_format, output_name)