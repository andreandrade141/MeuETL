import sys
from operation import ApiScrape


def main(qtd: int, fname: str, book: str, author: str) -> None:
    client = ApiScrape(url='https://www.abibliadigital.com.br/api/books')

    client.execute(qtd, fname)

    client.query_by_book(book)
    client.query_by_author(author)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print('Usage: run.py <qtd> <fname> <book> <author>')
