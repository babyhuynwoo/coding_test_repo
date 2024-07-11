
import random


if __name__ == '__main__':
    
    random_list = [random.randint(0, 100) for i in range(10)]

    print(random_list)

    for i in range(len(random_list)):
        min_index = i
        for j in range(i + 1,len(random_list)):
            if random_list[min_index] > random_list[j]:
                min_index = j
        random_list[i], random_list[min_index] = random_list[min_index], random_list[i]

    print(random_list)