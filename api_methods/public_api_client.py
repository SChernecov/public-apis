import random
import requests
from client.api_client import ApiClient


class PublicApiClient(ApiClient):

    def __init__(self, base_url):
        super().__init__(base_url)

    def get_entries(self):
        return self.get(path="entries")

    def get_random_entries_api(self):
        api = []
        r = self.get(path="entries")
        for entry in r.json()["entries"]:
            api.append(entry["API"])
        return random.choice(api)

    def get_random_entries_description(self):
        api = []
        r = self.get(path="entries")
        for entry in r.json()["entries"]:
            api.append(entry["Description"])
        return random.choice(api)

    def get_random_entries_category(self):
        api = []
        r = self.get(path="entries")
        for entry in r.json()["entries"]:
            api.append(entry["Category"])
        return random.choice(api)

    def get_random_entry(self):
        return self.get(path="random")

    def get_random_entry_param(self, **kwargs):
        params = {}
        params.update(**kwargs)
        return self.get(path="random", params=params)
