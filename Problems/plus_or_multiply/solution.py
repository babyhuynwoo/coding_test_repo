
def maximun_number(array):
    if not array:
        return 0
    
    if len(array) == 1:
        return array[0]

    pre = array[0]

    for i in range(1, len(array)):

        if pre < 2 or array[i] < 2:
            array[i] += pre
        else:
            array[i] *= pre 

        pre = array[i]

    return array[-1]

if __name__ == '__main__':

    # array = [0, 2, 9, 8, 4]
    array = [3, 4, 5, 2, 1, 9, 0]
    result = maximun_number(array)
        
    print(result)