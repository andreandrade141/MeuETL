import csv
import requests


class ApiScrape():
    def __init__(self, url: str) -> None:
        self.url = url

    def execute(self, quantity: int,  f_name: str) -> None:
        content = []
        c = 0
        r = requests.get(self.url)
        data = r.json()
        with open(f_name + '.' + 'csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Abreviação', 'Autor', 'Capítulos',
                             'Grupo', 'Nome', 'Testamento'])
            for c in range(quantity):
                writer.writerow([data[c]['abbrev'], data[c]['author'],
                                 data[c]['chapters'], data[c]['group'],
                                 data[c]['name'], data[c]['testament']])
            csvfile.close()
        pass
