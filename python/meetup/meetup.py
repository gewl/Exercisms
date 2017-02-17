import calendar, collections
from datetime import date

weekday_dict = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
    }

def meetup_day(year, month, day, which):
    calendar.setfirstweekday(weekday_dict[day])
    month_info = collections.deque(calendar.monthcalendar(year, month))
    if month_info[0][0] == 0:
        month_info.popleft()
    key = unicode(which[0], 'utf-8')
    if key.isnumeric():
        return date(year, month, month_info[int(key)-1][0])
    elif key == 't':
        if str(month_info[2][0]).startswith("1"):
            return date(year, month, month_info[2][0])
        else:
            return date(year, month, month_info[1][0])
    elif key == 'l':
        return date(year, month, month_info.pop()[0])
