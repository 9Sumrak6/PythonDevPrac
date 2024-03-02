import cowsay


monster = 'cow'

field = [[0 for j in range(10)] for i in range(10)]
x, y = 0, 0

while inp := input():
    inp = inp.split()

    moved = 0
    if inp[0] == 'up':
        y = (y - 1) % 10
        moved = 1
    elif inp[0] == 'down':
        y = (y + 1) % 10
        moved = 1
    elif inp[0] == 'right':
        x = (x + 1) % 10
        moved = 1
    elif inp[0] == 'left':
        x = (x - 1) % 10
        moved = 1

    if moved == 1:
        print(f'Moved to (<{x}><{y}>)')

        if field[y][x] == 1:
            func()

    inp[0] == 'addmon':
    else:
        print('Invalid command')


print(cowsay.cowsay('lala', cow=monster))