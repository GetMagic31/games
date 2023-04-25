def walk(direction, x_coor, y_coor):
    if direction == 'up' or 'down' or 'left' or 'right':
        if direction == 'up':
            y_coor -= 1
            return y_coor, x_coor
        if direction == 'down':
            y_coor += 1
            return y_coor, x_coor
        if direction == 'left':
            x_coor -= 1
            return y_coor, x_coor
        if direction == 'right':
            x_coor += 1
            return y_coor, x_coor
        if direction == 'stop' or 'Stop':
            exit()
    else:
        print("Please give a viable direction")

map = [
    [0, 0, 0, 2, 0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 2, 3, 0, 0, 0, 3, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 2, 0, 0, 0, 3, 0, 0, 9]
]
x_coor = 0
y_coor = 0
coor = (y_coor, x_coor)

position = map[y_coor][x_coor]
print(f'Your starting Coordinates are: {coor}')

while position != int(9):
    direction = input('In which direction do you want to walk? ')
    coor = walk(direction, x_coor, y_coor)
    print(f'Your Coordinates are: {coor}')
    y_coor, x_coor = coor[0], coor[1]
    position = map[y_coor][x_coor] 
    if position == 0:
        continue
    if position == 1:
        print('You walked into a waterplace, this is game over!')
        exit()
    if position == 2:
        print('You fell down a cliff, this is game over!')
        exit()
    if position == 3:
        print('Pirates attacked you, this is game over!')
        exit()
    if position == 9:
        print('Your are at your final destiantion!')
        exit()


