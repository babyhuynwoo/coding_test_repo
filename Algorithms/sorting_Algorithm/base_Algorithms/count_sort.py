
import random


if __name__ == '__main__':
    
    random_list = [random.randint(0, 100) for i in range(10)]

    print(random_list)

    count = [0] * (max(random_list) + 1)

    for i in range(len(random_list)):
        count[random_list[i]] += 1

    sorted_list = []
    
    for i in range(1, len(count)):
        for j in range(count[i]):
            sorted_list.append(i)

    print(sorted_list)