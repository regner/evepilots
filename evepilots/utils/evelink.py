

from datetime import datetime


def evelink_ts_to_datetime(ts):
    """ Converts a timestamp returned from EVE Link to a python
    datetime object.

    :param ts: A string timestamp from EVE Link.
    """

    return datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')
