# developed by strelnikov87
field_top_numbers = '  |' + ' | '.join('123456') + '|'
field = [['|O|'] * 6 for i in range(6)]


class MyException(Exception):
    pass


class Dot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot({self.x, self.y})'

class Ship:
    def __init__(self, coord_1:int, coord_2:int):
        self._coord_1 = coord_1
        self._coord_2 = coord_2
        self._health = 100


    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        self._health = new_health

    @property
    def coords(self):
        return self._coord_1, self._coord_2

def show_field():
    print(field_top_numbers)
    for k, v in enumerate(field):
        print(k + 1, *v)

show_field()
ship_1 = Ship(3, 1)
print(ship_1.health)
ship_1.health = 50
print(ship_1.health)
