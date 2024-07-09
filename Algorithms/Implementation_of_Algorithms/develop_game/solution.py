def rotate(direction, n=1):

    directions = [0, 1, 2, 3]

    direction -= n
    direction = directions[direction]
    return direction

def move(x, y, direction):

    move_per_direction = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}

    x_ = x + move_per_direction[direction][0]
    y_ = y + move_per_direction[direction][1] 

    return x_, y_

def game_develop(map_info, x, y, direction):

    count = 0 
    direction_check = 0
    map_info[x][y] -= 1 

    while(True):

        x_, y_ = move(x, y, rotate(direction))

        if map_info[x_][y_] == 0:
            direction = rotate(direction)
            x, y = x_, y_
            map_info[x][y] -= 1 
            count += 1
            direction_check = 0
        else:
            direction = rotate(direction)

        if direction_check == 4:

            reverse_direction = rotate(direction, 2)
            x_, y_ = move(x, y, reverse_direction)

            if map_info[x_][y_] != 1 and map_info[x_][y_] >= -1:
                x = x_
                y = y_
                count += 1
                direction_check = 0
                map_info[x][y] -= 1
            else:
                break

        direction_check += 1
        
    return count

def input_game_develop():
    N, M = [int(num) for num in input('first input(N, M): ').split()]
    x, y, direction = [int(num) for num in input('second input(x, y, face direction): ').split()]

    map_info = []
    for _ in range(N):
        row = [int(num) for num in input(f'map row:{_}(N): ').split()]
        map_info.append(row)

    return map_info, x, y, direction