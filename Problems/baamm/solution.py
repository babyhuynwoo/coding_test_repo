

def print_2d_matrix(array):

    for row in array:
        print(row)
    print()

if __name__ == '__main__':

    N = 6
    K = 3
    apple_loc = [[3,4],[2,5],[5,3]]
    rotate_time = [[3,"D"],[15,"L"],[17,"D"]]

    matrix = [[0 for i in range(N)] for j in range(N)]

    for loc in apple_loc:
        _x = loc[0] - 1
        _y = loc[1] - 1
        matrix[_x][_y] = 1

    head = [0,0,0]
    
    dir_list = ["left",  "up", "right", "down"]
    direction = 2

    sec = 0 
    tail_list = []

    while True:
        sec += 1

        if head[0] >= N or head[1] >= N or head[0] < 0 or head[1] < 0 or matrix[head[0]][head[1]] == -1:
            break
        else:
            temp = matrix[head[0]][head[1]]
            matrix[head[0]][head[1]] = 'H'
            print_2d_matrix(matrix)
            matrix[head[0]][head[1]] = temp
            for tail in tail_list:
                matrix[tail[0]][tail[1]] = 0
            tail_list = []

        if matrix[head[0]][head[1]] == 1:
            head[2] += 1
            matrix[head[0]][head[1]] = 0 

        if head[2] != 0:
            tail_list = tail_list[:-2]
            tail_list.append([head[0],head[1]])

        i = 0

        if sec == rotate_time[i][0]:
            if rotate_time[i][1] == 'D':
                direction += 1
            elif rotate_time[i][1] == 'L':
                direction -= 1
            i += 1

        if dir_list[direction] == 'right':
            head[1] += 1
        elif dir_list[direction] == 'left':
            head[1] -= 1
        elif dir_list[direction] == 'up':
            head[0] -= 1
        elif dir_list[direction] == 'down':
            head[0] += 1

        for tail in tail_list:
            matrix[tail[0]][tail[1]] = -1

    print(sec)