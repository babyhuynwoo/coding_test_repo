def royal_knight(column, row):

    cur_pos = [column, row]

    count = 0

    moving = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

    for move in moving:    
        if (cur_pos[0] + move[0] >= 1) and (cur_pos[1] + move[1] >= 1) and (cur_pos[0] + move[0] <= 8) and (cur_pos[1] + move[1] <= 8):
            count += 1

    return count

def input_royal_knight():
        
    N = input('first input (N): ')

    table = {}

    for _, num  in zip(list('abcdefgh'), range(8)):
        table[_] = num + 1
    
    column = table[N[0]]
    row = int(N[1])

    return column, row