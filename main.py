# developed by strelnikov87
import classes as clss


# def show_field():
#     for k, v in enumerate(field):
#         print(k + 1, *v)

def welcome_to_the_game():
    print('Welcome to the WarShip game!')
    print('Enter: x y')
    print('x - row number')
    print('y - column number')


def start_game():
    user_move = True
    while True:
        print('*' * 27)
        print('User board:')
        print(game.user.board)
        print('*' * 27)
        print('PC board: ')
        print(game.ai.board)
        print('*' * 27)
        if user_move:
            print('User move!')
            game.user.move()
            user_move = False
        else:
            print('PC move!')
            game.ai.move()
            user_move = True

        if game.ai.board.count == len(game.ai.board.ships):
            print('*' * 27)
            print('User won!!!')
            break

        if game.user.board.count == len(game.user.board.ships):
            print('*' * 27)
            print('PC won!!!')
            break

game = clss.Game()
welcome_to_the_game()
start_game()
