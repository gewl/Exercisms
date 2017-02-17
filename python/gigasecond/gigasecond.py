from datetime import datetime, timedelta, date
import math

def add_gigasecond(birth):
    origin_date = datetime.fromtimestamp(0)
    birth_seconds = (birth - origin_date).total_seconds()
    gigasecond_added = birth_seconds + math.pow(10, 9)
    return datetime.fromtimestamp(gigasecond_added)
