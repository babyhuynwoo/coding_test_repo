def input_up_down_left_right():
    
    N = int(input('first input (N): '))
    moving_plan = input('second input (moving plan): ').split()
    
    return N, moving_plan

def up_down_left_right(N, moving_plan):
    
    start_point = [1,1]
    
    for move in moving_plan:
        if move == 'R' and start_point[1] < N:
            start_point[1] += 1
        elif move == 'U' and start_point[0] > 1:
            start_point[0] -= 1
        elif move == 'L' and start_point[1] > 1:
            start_point[1] -= 1
        elif move == 'D' and start_point[0] < N:
            start_point[0] += 1
    
    return start_point


if __name__ == '__main__':
    N, moving_plan = input_up_down_left_right()
    print(up_down_left_right(N, moving_plan)) 