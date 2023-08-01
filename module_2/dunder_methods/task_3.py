from datetime import datetime

class TimeInterval:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __contains__(self, date):
        self.date = date
        return self.start_date <= date <= self.end_date


time_1 = TimeInterval(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31))

if datetime(2023, 10, 30) in time_1:
    print("It's there")
else:
    print("It's not there")
