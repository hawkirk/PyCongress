from .client import Client
from .utils import CURRENT_CONGRESS


class BillClient(Client):

    def get(self, bill_type=None, bill_number=None, congress=CURRENT_CONGRESS, return_type=None):
        if congress and bill_type and bill_number and return_type:
            path = "bill/{}/{}/{}/{}.json".format(
                congress, bill_type, bill_number, return_type
            )
        elif congress and bill_type and bill_number:
            path = "bill/{}/{}/{}.json".format(
                congress, bill_type, bill_number
            )
        elif congress and bill_type:
            path = "bill/{}/{}.json".format(
                congress, bill_type
            )
        elif congress:
            path = "bill/{}.json".format(congress)
        else:
            path = "bill.json"
        return self.fetch(path)

    def list_bills(self, congress=None, bill_type=None):
        """
        Returns a list of bills sorted by date of latest action, optionally
        limited by congress and/or bill type.
        """
        if congress and bill_type:
            return self.get(
                congress=congress,
                bill_type=bill_type)
        elif congress:
            return self.get(congress=congress)

        return self.get()

    def bill_info(self, bill_type, bill_number, congress=CURRENT_CONGRESS, return_type=None):
        """
        Returns detailed information for a specified bill. Optionally returns
        additional bill information: actions, amendments, committees,
        cosponsors, related bills, subjects, summaries, text versions, and/or
        titles.
        """
        return_types = [
            'actions',
            'amendments',
            'committees',
            'cosponsors',
            'relatedBills',
            'subjects',
            'summaries',
            'text',
            'titles']
        if return_type:
            if return_type not in return_types:
                raise ValueError("Invalid return type. Expected one of %s" % return_types)
            return self.get(
                congress=congress,
                bill_type=bill_type,
                bill_number=bill_number,
                return_type=return_type)
        return self.get(
            congress=congress,
            bill_type=bill_type,
            bill_number=bill_number)
