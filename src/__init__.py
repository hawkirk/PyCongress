"""
Python client for the Congress.gov API
API Docs: ______________
"""
__author__ = "harrison kirk (github.com/hawkirk)"
__version__ = "0.0.0"

import os

class Congress(Client):
    """
    text
    """
    
    def __init__(self, apikey=None, http=None):
        if apikey is None:
            apikey = os.environ.get('CONGRESS_API_KEY')

    # self.bill
    # self.amendments
    # self.summaries
    # self.congress
    # self.member
    # self.committee
    # self.committee_report
    # self.congressional_record
    # self.house_communication
    # self.nomination
    # self.treaty
    