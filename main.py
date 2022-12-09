field_top_numbers = '  |' + ' | '.join('123456') + '|'
field = [['|O|'] * 6 for i in range(6)]


def show_field():
    print(field_top_numbers)
    for k, v in enumerate(field):
        print(k + 1, *v)

show_field()