from .client import Client
from .utils import CURRENT_CONGRESS

class BillClient(Client):

    def get(self, bill_type, bill_number, congress=CURRENT_CONGRESS, data=None):
        if data:
            path = f"bill/{congress}/{bill_type}/{bill_number}/{data}.json"
        
        else:
            path = f"bill/{congress}/{bill_type}/{bill_number}.json"

        return self.fetch(path)

    def actions(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(congress, bill_type, bill_number, data="actions")