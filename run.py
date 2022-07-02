from operation import ApiScrape


def main() -> None:
    client = ApiScrape(url='https://www.abibliadigital.com.br/api/books')

    client.execute(quantity=50, f_name='extract')

    client.query_by_book('Rute')
    client.query_by_author('Samuel')


if __name__ == '__main__':
    main()
