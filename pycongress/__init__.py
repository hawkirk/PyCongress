"""
Python client for the Congress.gov API
API Docs: https://api.congress.gov/#/
"""
__author__ = "harrison kirk (hawkirk)"
__version__ = "0.0.0"

import os

from .client import Client
from .utils import CURRENT_CONGRESS, get_congress, df_output

# subclients
from .bill import BillClient
from .member import MemberClient
from .congress import CongressClient


__all__ = ('Congress', 'get_congress', 'df_output', 'CURRENT_CONGRESS')


class Congress(Client):

    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.environ.get('CONGRESS_API_KEY')

        super(Congress, self).__init__(api_key)

        self.bill = BillClient(self.api_key)
        self.member = MemberClient(self.api_key)
        self.congress = CongressClient(self.api_key)
