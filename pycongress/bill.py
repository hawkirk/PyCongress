from .client import Client
from .utils import CURRENT_CONGRESS

class BillClient(Client):

    def get(self, bill_type, bill_number, congress=CURRENT_CONGRESS, data=None):
        if data:
            path = "bill/{}/{}/{}/{}.json".format(
                congress, bill_type, bill_number, data
            )

        else:
            path = "bill/{}/{}/{}/{}.json".format(
                congress, bill_type, bill_number, data
            )

        return self.fetch(path)

    def actions(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(
            congress=congress,
            bill_type=bill_type,
            bill_number=bill_number,
            data="actions"
            )

    def amendments(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(congress, bill_type, bill_number, data="amendments")

    def committees(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(congress, bill_type, bill_number, data="comittees")

    def cosponsors(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(congress, bill_type, bill_number, data="cosponsors")
