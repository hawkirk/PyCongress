from .client import Client
from .utils import CURRENT_CONGRESS


class BillClient(Client):

    def get(self, bill_type, bill_number, congress=CURRENT_CONGRESS, data=None):
        if data:
            path = "bill/{}/{}/{}/{}.json".format(
                congress, bill_type, bill_number, data
            )

        else:
            path = "bill/{}/{}/{}.json".format(
                congress, bill_type, bill_number
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
        return self.get(
            congress=congress,
            bill_type=bill_type,
            bill_number=bill_number,
            data="amendments")

    def committees(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(
            congress=congress,
            bill_type=bill_type,
            bill_number=bill_number,
            data="committees")

    def cosponsors(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(
            congress=congress,
            bill_type=bill_type,
            bill_number=bill_number,
            data="cosponsors")

    def related_bills(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(
            congress=congress,
            bill_type=bill_type,
            bill_number=bill_number,
            data="relatedbills")

    def subjects(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(
            congress=congress,
            bill_type=bill_type,
            bill_number=bill_number,
            data="subjects")

    def summaries(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(
            congress=congress,
            bill_type=bill_type,
            bill_number=bill_number,
            data="summaries")

    def text(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(
            congress=congress,
            bill_type=bill_type,
            bill_number=bill_number,
            data="text")

    def titles(self, bill_type, bill_number, congress=CURRENT_CONGRESS):
        return self.get(
            congress=congress,
            bill_type=bill_type,
            bill_number=bill_number,
            data="titles")
