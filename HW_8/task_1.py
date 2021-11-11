#задание 1
class Date:
    # data = ''
    def __init__(self, date):
        self.date = date
    @classmethod
    def int_method (cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year
    @staticmethod
    def test_method (date):
        day, month, year = map(int, date.split('-'))
        return day<=31 and month<=12 and year<= 2022



a = Date('08-10-2021')
print(Date.int_method('08-10-2021'))
print(Date.test_method('08-10-2021'))
print(a.date)

