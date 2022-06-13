import json
from operation import ApiScrape


def main() -> None:
    client = ApiScrape(url='https://www.abibliadigital.com.br/api/books')

    client.execute(quantity=15)

    client.upload(f_name='')
    pass


if __name__ == '__main__':
    main()
