

if __name__ == "__main__":

    # sample = [3,2,1,1,9]
    data = [1,1,3,4,10,15]

    data.sort()

    target = 1
    for x in data:
        if target < x:
            break
        target += x

    print(target)