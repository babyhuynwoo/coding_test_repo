
def adventurers_guild_1(array):
    array.sort(reverse=True)

    count = 0

    while array:
        if array[0] > len(array):
            break
    
        temp = array[0]
        array = array[temp:]
        count += 1

    return count

def adventurers_guild_2(party):

    party.sort()

    count = 0
    cur_groun_size = 0

    for member in party:

        cur_groun_size += 1

        if cur_groun_size >= member:
            count += 1
            cur_groun_size = 0

    return count


def get_input():
    N = int(input('input N: '))

    array = [int(user_input) for user_input in input('input array: ').split()]

    return N, array

if __name__ == '__main__':
    
    N, array = get_input()

    result_1 = adventurers_guild_1(array)
    result_2 = adventurers_guild_2(array)

    print(result_1)
    print(result_2)
