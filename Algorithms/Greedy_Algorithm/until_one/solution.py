def input_until_one():

    N, K = [int(_) for _ in input('first input (N, K): ').split()]

    return N, K

def until_one(N, K):

    count = 0

    while(N != 1):
        
        if N % K == 0:
            N = N//K
        else:
            N = N - 1

        count = count + 1

    return count

def until_one_advance(N, K):

    count = 0

    while(N != 0):
        
        if N % K == 0:
            N = N//K
            count = count + 1
        else:
            minus_need = N % K

            if minus_need == N :
                count = count + N - 1
                break
            
            count = count + minus_need
            N = N - minus_need

    return count