
def rotate(key, key_length):
    
    key = T(key, key_length)

    result = []

    for row in key:
        result.insert(0, list(reversed(row)))

    return result
    
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def T(array, array_length):
    array = [[array[i][j] for i in range(array_length)] for j in range(array_length)]

    return array

def shift_right(key, key_length):
    
    key = T(key, key_length)

    new_row = [0 for _ in range(key_length)]

    key.pop(-1)
    key.insert(0, new_row)

    key = T(key, key_length)

    return key

def shift_down(key, key_length):
    new_row = [0 for _ in range(key_length)]

    key.pop(-1)
    key.insert(0, new_row)

    return key

def sum_matrix(lock, key, lock_length):

    for i in range(lock_length):
        for j in range(lock_length):
            lock[i][j] += key[i][j]
            if lock[i][j] != 1:
                lock[i][j] -= key[i][j]
                return False

    return True

def check_match(lock, key):

    lock_length = len(lock)
    key_length = len(key)

    keys = [key]

    for _ in range(3):
        key = rotate(key, key_length)
        keys.append(key)

    for key in keys:
        if sum_matrix(lock, key, lock_length):
            return True
        for _ in range(lock_length):    
            key = shift_right(key, key_length)
            if sum_matrix(lock, key, lock_length):
                    return True
            for _ in range(lock_length):
                key = shift_down(key, key_length)
                if sum_matrix(lock, key, lock_length):
                    return True

    return False

if __name__ == '__main__':

    lock = [[1,1,1], [1,1,0], [1,0,1]]
    # key = [[0,0,0], [1,0,0], [0,1,1]]
    key = [[1,0], [0,1]]

    lock_length = len(lock)

    temp = [[0 for _ in range(lock_length)] for _ in range(lock_length)]        

    key_length = len(key)

    for i in range(key_length):
        for j in range(key_length):
            temp[i][j] = key[i][j]

    key = temp

    if check_match(lock, key):
        print("true")
    else:
        print("false")
