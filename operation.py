import csv
import requests

from pprint import pprint


class ApiScrape():
    def __init__(self, url: str) -> None:
        self.url = url

    def request_data(self) -> None:
        r = requests.get(self.url)
        self.data = r.json()

    def write_csvfile(self, quantity: int, f_name: int) -> None:
        c = 0
        with open(f_name + '.' + 'csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Abreviação', 'Autor', 'Capítulos',
                             'Grupo', 'Nome', 'Testamento'])
            for c in range(quantity):
                writer.writerow([self.data[c]['abbrev'], self.data[c]['author'],
                                 self.data[c]['chapters'], self.data[c]['group'],
                                 self.data[c]['name'], self.data[c]['testament']])

    def query_by_book(self, book: str) -> None:
        with open('extract.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            pprint(
                '-----------------------------------------------------')
            pprint(f'Livros com o nome de: {book}')
            for row in reader:
                try:
                    if row[4] == book:
                        pprint(row)
                except ValueError:
                    raise ValueError('Livro não encontrado')

    def query_by_author(self, author: str) -> None:
        with open('extract.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            pprint(
                '-----------------------------------------------------')
            pprint(f'Livros escritos por: {author}')
            for row in reader:
                try:
                    if row[1] == author:
                        pprint(row)
                except ValueError:
                    raise ValueError('Autor não encontrado')

    def execute(self, quantity: int,  f_name: str) -> None:
        self.request_data()
        self.write_csvfile(quantity, f_name)
