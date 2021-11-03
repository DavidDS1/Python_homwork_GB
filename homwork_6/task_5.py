#задание 5
class Stationery:
    title = 'Пейзаж Сибири'
    def draw (self):
        print('Запуск отрисовки')
class Pen (Stationery):
    def draw (self):
        print('Ручкой рисуем озеро байкал')
class Pencil (Stationery):
    def draw (self):
        print('Карандашом рисуем сибирский лес')
class Handle (Stationery):
    def draw (self):
        print('Маркером закрашиваем рисунок')

print(Stationery.title)
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()