import json
from typing import List
import requests


class ApiScrape():
    def __init__(self, url: str) -> None:
        self.url = url

    def execute(self, quantity: int) -> List[str]:
        self.content = []
        data = requests.get(self.url)
        json_data = json.load(data)
        print(json_data)
        # for i in json_data:
        #     if(len(self.content) >= quantity):
        #         break

        #     self.content.append(i)

    # def upload(self, f_name: str) -> None:

    #     pass
