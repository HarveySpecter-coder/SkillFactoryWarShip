import exceptions as exc
from random import randint

class Dot:
    def __init__(self, x: int, y: int):
        self.y = y
        self.x = x


    def __eq__(self, other) -> bool:
        if not isinstance(other, Dot):
            raise exc.BoardExcept('It isn"t Dot object')
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> hash:
        return hash(id(self))


    def __repr__(self) -> str:
        return f'Dot{self.x, self.y}'

class Ship:
    def __init__(self, bow: Dot, lenght: int, orientation: int):
        self.bow = bow
        self.orientation = orientation
        self.lenght = lenght
        self.orientation = orientation
        self.health = lenght

    @property
    def ship_dots(self) -> list:
        ship_dots = []
        for i in range(self.lenght):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.orientation == 0:
                cur_x+= i
            elif self.orientation == 1:
                cur_y+= i

            ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots

    def shooten(self, shot: Dot):
        return shot in self.ship_dots
    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, new_health: int):
        self._health = new_health


class Board:
    def __init__(self, hid: bool = False, size: int = 6):
        self.hid = hid
        self.size = size
        self.count = 0
        self.field = [['O'] * size for _ in range(size)]
        self.busy = []
        self.ships = []

    def __str__(self) -> str:
        res = '  | ' + ' | '.join('123456') + ' |'
        for k, v in enumerate(self.field):
            res+= f'\n{k + 1} | ' + ' | '.join(v) + ' |'

        if self.hid:
            res = res.replace('■', 'O')
        return res

    def out(self, dot:Dot) -> bool:
        return not((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def contour(self, ship: Ship, verb: bool = False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.ship_dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = '.'
                    self.busy.append(cur)

    def add_ship(self, ship:Ship):
        for d in ship.ship_dots:
            if self.out(d) or d in self.busy:
                raise exc.BoardShipExcept()
        for d in ship.ship_dots:
            self.field[d.x][d.y] = '■'
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, dot:Dot) -> bool:
        if self.out(dot):
            raise exc.BoardOutsideExcept()
        if dot in self.busy:
            raise exc.BoardShipExcept

        self.busy.append(dot)

        for ship in self.ships:
            if ship.shooten(dot):
                ship.health-= 1
                self.field[dot.x][dot.y] = 'X'
                if ship.health == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("The ship sank")
                    return False
                else:
                    print('The ship is wounded')
                    return True
        self.field[dot.x][dot.y] = '.'
        print('Away')
        return False

    def begin(self):
        self.busy = []


class Player:
    def __init__(self, board: Board, enemy: Board):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self) -> bool:
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except exc.BoardExcept as e:
                print(e)


class AI(Player):
    def ask(self) -> Dot:
        dot = Dot(randint(0,5), randint(0,5))
        print(f'PC move: {dot.x+1} {dot.y+1}')
        return dot

class User(Player):
    def ask(self) -> Dot:
        while True:
            coords = input('Your move: ').split()
            if len(coords) != 2:
                print('Enter two coords!')
                continue

            x, y = coords

            if not(x.isdigit()) or not (y.isdigit()):
                print('Enter numbers!')
                continue

            x, y = int(x), int(y)
            return Dot(x-1, y - 1)


class Game:
    def __init__(self, size:int = 6):
        self.size = size
        player = self.try_board()
        computer = self.try_board()
        computer.hid = True

        self.ai = AI(computer, player)
        self.user = User(player, computer)
    def try_board(self) -> Board:
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempt = 0
        for ln in lens:
            while True:
                if attempt > 1000:
                    print('Too many attempts! Trying create boards again...')
                    self.try_board()
                    break
                ship = Ship(bow = Dot(randint(0, self.size), randint(0, self.size)), lenght=ln, orientation=randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except exc.BoardShipExcept:
                    attempt+=1
        board.begin()
        return board