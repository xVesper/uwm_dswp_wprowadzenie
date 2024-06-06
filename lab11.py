import re
from datetime import datetime
import requests
import csv
import pickle

'''Zadanie 1'''
def search_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        numbers = re.findall(r'\b\d+\b', content)
        print("Wszystkie liczby:", numbers)

        numbers_3digits = re.findall(r'\b\d{3,}\b', content)
        print("Wszystkie liczby co najmniej 3 cyfrowe:", numbers_3digits)

        ipv4_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', content)
        print("Wszystkie adresy IPv4:", ipv4_addresses)

        capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', content)
        print("Wszystkie wyrazy rozpoczynające się od wielkiej litery:", capitalized_words)

        lines_with_min_four_words = re.findall(r'^(?:\S+\s+){3}\S+', content, re.MULTILINE)
        print("Wszystkie linie z co najmniej 4 wyrazami:", lines_with_min_four_words)

        urls = re.findall(r'\bhttps?:\/\/[^\s]+', content)
        print("Wszystkie adresy URL:", urls)

search_in_file('strings.txt')


'''Zadanie 2'''

url = "https://raw.githubusercontent.com/elastic/examples/master/Machine%20Learning/Security%20Analytics%20Recipes/suspicious_login_activity/data/auth.log"
response = requests.get(url)
with open("auth.log", "w") as file:
    file.write(response.text)

def parse_log_to_csv(log_path, csv_path):
    with open(log_path, 'r') as log_file, open(csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Date', 'IP', 'Service/User', 'Message'])
        log_pattern = re.compile(
            r'(?P<date>\w{3} \d{1,2} \d{2}:\d{2}:\d{2})'
            r'.*\['
            r'(?P<pid>\d+)'
            r'\]: '
            r'(?P<msg>.*)'
        )

        for line in log_file:
            match = log_pattern.search(line)
            if match:
                date = datetime.strptime(match.group('date'), "%b %d %H:%M:%S")
                date = date.replace(year=datetime.now().year).strftime('%Y-%m-%d %H:%M:%S')
                message = match.group('msg')
                ip_match = re.search(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', line)
                ip = ip_match.group(0) if ip_match else ''

                service_user_search = re.search(r'^\w+', message)
                if service_user_search:
                    service_user = service_user_search.group(0)
                else:
                    service_user = 'Unknown'

                csv_writer.writerow([date, ip, service_user, message])

log_path = 'auth.log'
csv_path = 'parsed_auth_log.csv'

parse_log_to_csv(log_path, csv_path)

'''Zadanie 3'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says woof!"

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}"
def save_object(obj, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

dog = Dog("Rex", 5)
save_object(dog, 'dog.pickle')
print("Saved dog to file.")
def load_object(filename):
    with open(filename, 'rb') as inp:
        return pickle.load(inp)

loaded_dog = load_object('dog.pickle')
print("Loaded dog from file.")
print(loaded_dog)
print(loaded_dog.speak())

'''Zadanie 4'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says woof!"

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}"

def save_objects(objects, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(objects, outp, pickle.HIGHEST_PROTOCOL)

def load_objects(filename):
    with open(filename, 'rb') as inp:
        return pickle.load(inp)
dogs = [
    Dog("Rex", 5),
    Dog("Buddy", 2),
    Dog("Maggie", 7),
    Dog("Annie", 3)
]
save_objects(dogs, 'dogs.pickle')
print("Saved list of dogs to file.")
loaded_dogs = load_objects('dogs.pickle')
print("Loaded list of dogs from file:")
for dog in loaded_dogs:
    print(dog)
    print(dog.speak())