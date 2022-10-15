from .client import Client
from .utils import CURRENT_CONGRESS


class CongressClient(Client):

    def get(self, congress=None):
        if congress:
            path = "congress/{}.json".format(congress)
        else:
            path = "congress.json"
        return self.fetch(path)

    def list_sessions(self):
        """
        Returns a list of congresses and congressional sessions.
        """
        return self.get()

    def congress_info(self, congress=CURRENT_CONGRESS):
        """
        Returns detailed information for a specified congress.
        """
        return self.get(
            congress=congress)
