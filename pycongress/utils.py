"""
helper functions and error handling
"""
import datetime
import math

def get_congress(year):
    if year < 1789:
        raise ValueError

    return int(math.floor((year - 1789) / 2 + 1))

CURRENT_CONGRESS = get_congress(datetime.datetime.now().year)