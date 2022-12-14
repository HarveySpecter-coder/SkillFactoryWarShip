class BoardExcept(Exception):
    pass


class BoardOutsideExcept(BoardExcept):
    def __str__(self) -> str:
        return 'You"re trying to shoot outside the board!'


class BoardShootedExcept(BoardExcept):
    def __str__(self) -> str:
        return 'You shot at this point!'


class BoardShipExcept(BoardExcept):
    pass
