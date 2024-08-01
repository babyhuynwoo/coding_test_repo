
import random


if __name__ == '__main__':
    
    random_list = [random.randint(0, 100) for i in range(10)]

    print(random_list)
    
    for i in range(1, len(random_list)):
        for j in range(i, 0, -1):
            if random_list[j] < random_list[j - 1]:
                random_list[j], random_list[j - 1] = random_list[j - 1], random_list[j]
            else:
                break

    print(random_list)