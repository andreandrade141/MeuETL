from operation import ApiScrape


def main() -> None:
    client = ApiScrape(url='https://www.abibliadigital.com.br/api/books')

    client.execute(quantity=50, f_name='extract')


if __name__ == '__main__':
    main()
