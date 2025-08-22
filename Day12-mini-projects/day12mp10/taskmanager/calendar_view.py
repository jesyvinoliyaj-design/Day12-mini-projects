import calendar
from datetime import datetime

def show_calendar(year=None, month=None):
    if not year or not month:
        today = datetime.now()
        year, month = today.year, today.month
    print(f"\n📅 Calendar for {month}/{year}\n")
    print(calendar.month(year, month))
