import pytest
import allure
from helpers.random_helper import random_punctuations, random_whitespaces, \
    random_int, random_bool


@allure.feature("Test entries")
class TestPublicApiEntries:

    def test_get_entries(self, client):
        r = client.get_entries()

        assert r.status_code == 200, "Wrong status code"

    def test_entries_count(self, client):
        r = client.get_entries()

        assert r.status_code == 200, "Wrong status code"
        assert r.json()["count"] == len(r.json()["entries"]), \
            "Wrong len entries count"

    def test_random_entry(self, client):
        r = client.get_random_entry()

        assert r.status_code == 200, "Wrong status code"


@allure.feature("Test entries title")
class TestPublicApiEntriesTitle:
    def test_random_entry_title(self, client):
        random_api = client.get_random_entries_api()

        r = client.get_random_entry_param(title=random_api)
        assert r.status_code == 200, "Wrong status code"
        for api in r.json()["entries"]:
            assert api["API"] == random_api

    @pytest.mark.parametrize("title", [random_punctuations(),
                                       random_whitespaces(),
                                       random_bool()],
                             ids=["random_punctuations",
                                  "random_whitespaces",
                                  "random_bool"])
    def test_invalid_random_entry_title(self, client, title):
        r = client.get_random_entry_param(title=title)

        assert r.status_code == 400, "wrong status code"


@allure.feature("Test entries description")
class TestPublicApiEntriesDescription:
    def test_random_entry_description(self, client):
        random_description = client.get_random_entries_description()

        r = client.get_random_entry_param(description=random_description)
        assert r.status_code == 200, "Wrong status code"
        for api in r.json()["entries"]:
            assert api["Description"] == random_description

    @pytest.mark.parametrize("description", [random_punctuations(),
                                             random_whitespaces()],
                             ids=["random_punctuations",
                                  "random_whitespaces"])
    def test_invalid_random_entry_description(self, client, description):
        r = client.get_random_entry_param(description=description)
        assert r.status_code == 400, "wrong status code"

@allure.feature("Test entries cors")
class TestPublicApiEntriesCors:
    @pytest.mark.parametrize("cors", ["yes", "no", "unknown"],
                             ids=["yes",
                                  "no",
                                  "unknown"])
    def test_random_entry_cors(self, client, cors):
        r = client.get_random_entry_param(cors=cors)
        assert r.status_code == 200, "Wrong status code"

    @pytest.mark.parametrize("cors", [random_punctuations(),
                                      random_whitespaces(),
                                      random_int(),
                                      random_bool(),
                                      0],
                             ids=["random_punctuations",
                                  "random_whitespaces",
                                  "random_int",
                                  "random_bool",
                                  "zero"])
    def test_invalid_random_entry_cors(self, client, cors):
        r = client.get_random_entry_param(cors=cors)
        assert r.status_code == 400, "Wrong status code"

@allure.feature("Test entries category")
class TestPublicApiEntriesCategory:
    def test_random_entry_category(self, client):
        random_category = client.get_random_entries_category()

        r = client.get_random_entry_param(category=random_category)
        assert r.status_code == 200, "Wrong status code"
        for api in r.json()["entries"]:
            assert api["Category"] == random_category

    @pytest.mark.parametrize("category", [random_punctuations(),
                                          random_whitespaces(),
                                          random_int(),
                                          random_bool(),
                                          0],
                             ids=["random_punctuations",
                                  "random_whitespaces",
                                  "random_int",
                                  "random_bool",
                                  "zero"])
    def test_invalid_random_entry_category(self, client, category):
        r = client.get_random_entry_param(category=category)
        assert r.status_code == 400, "wrong status code"
