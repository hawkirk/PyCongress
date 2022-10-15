"""
Base client to fetch responses from the API
"""
import requests


class Client(object):

    # top-level api url
    BASE_URL = "https://api.congress.gov/v3/"

    def __init__(self, api_key=None, limit='100'):
        self.api_key = api_key
        self.limit = limit

    def fetch(self, path):
        """
        Fetch response from the api based on a specified path.
        """
        headers = {"X-API-Key": self.api_key}
        url = self.BASE_URL + path + '?limit=' + self.limit
        content = requests.get(url=url, headers=headers).json()
        return content
