from operation import ApiScrape


class Test:
    def instance_tests(self):
        api = ApiScrape(url='https://www.abibliadigital.com.br/api/books')
        assert isinstance(api, ApiScrape)
        assert api.url == 'https://www.abibliadigital.com.br/api/books'

    def types_test(self):
        api = ApiScrape(url='https://www.abibliadigital.com.br/api/books')
        assert api.quantity == type(int)
        assert api.f_name == type(str)
