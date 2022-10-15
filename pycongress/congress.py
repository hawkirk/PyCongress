from .client import Client
from .utils import CURRENT_CONGRESS


class CongressClient(Client):

    def get(self, congress=CURRENT_CONGRESS):
        if congress:
            path = "congress/{}.json".format(congress)
        else:
            path = "congress.json"
        return self.fetch(path)

    def list_sessions(self):
        return self.get()

    def info(self, congress):
        return self.get(
            congress=congress)
