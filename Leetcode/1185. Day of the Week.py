import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = datetime.datetime(year, month, day)
        return d.strftime("%A")
