#задание 3
class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income
class Position (Worker):
    def get_full_name (self):
        print(f'{self.surname} {self.name}')
    def get_total_income (self):
        print(self._income.get('wage') + self._income.get('bonus'))

worker_1 = Position('Ivan', 'Zakharov', 'engineer', {'wage': 50000, 'bonus': 10000})
worker_1.get_full_name()
worker_1.get_total_income()