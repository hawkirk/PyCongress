"""
base client to fetch responses from the API
"""
import json
import requests
from requests import auth

class Client(object):
    
    # top-level api url
    base_url = "https://api.congress.gov/v3/"
    
    def __init__(self, api_key=None):
        self.api_key = api_key

    def fetch(self, path):
        """
        Fetch response from the api based on specified path
        """

        headers = {"X-API-Key": self.api_key}
        url = self.base_url + path
        
        content = requests.get(url=url, headers=headers).json()

        return content

