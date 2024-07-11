

def swap_array(arr_1, arr_2, k):

    arr_1.sort()
    arr_2.sort(reverse = True)

    for i in range(k):
        if arr_1[i] < arr_2[i]:
            arr_1[i] = arr_2[i]
        else:
            break

    return sum(arr_1)
