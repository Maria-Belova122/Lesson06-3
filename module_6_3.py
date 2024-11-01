# ЗАДАНИЕ ПО ТЕМЕ "Множественное наследование"

class Horse:

    def __init__(self):
        self.x_distance = 0  # пройденный лошадью путь
        self.sound = 'Frrr'  # звук, издаваемый лошадью

    def run(self, dx):
        self.x_distance += dx  # изменение пройденного пути


class Eagle:

    def __init__(self):
        self.y_distance = 0  # высота полета орла
        self.sound = 'I train, eat, sleep, and repeat'  # звук, издаваемый орлом

    def fly(self, dy):
        self.y_distance += dy  # изменение высоты полета


class Pegasus(Horse, Eagle):

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    # изменение координат пегаса
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    # текущее положение пегаса (текущие координаты)
    def get_pos(self):
        current_position = (self.x_distance, self.y_distance)
        return current_position

    # унаследованный звук
    def voice(self):
        print(self.sound)


# print(Pegasus.mro())

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
