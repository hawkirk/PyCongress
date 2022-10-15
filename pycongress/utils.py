"""
helper functions and error handling
"""
import pandas as pd
import datetime
import math


def get_congress(year):
    """
    Returns the congress number based on a specified year.
    """
    if year < 1789:
        raise ValueError

    return int(math.floor((year - 1789) / 2 + 1))


def df_output(json_input):
    """
    Takes json request output and returns a pandas DataFrame object.
    """
    df = pd.DataFrame(json_input["result"])
    return df


CURRENT_CONGRESS = get_congress(datetime.datetime.now().year)
