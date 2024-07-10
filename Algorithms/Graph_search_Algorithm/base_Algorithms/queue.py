from collections import deque

if __name__ == '__main__':
    queue = deque()

    queue.append(1)
    queue.append(2)
    queue.append(3)


    print('Initial queue')
    print(queue)
    queue.reverse()
    print(queue)

    print('\nElements removed from queue:')
    print(queue.popleft())
    print(queue.popleft())
    print(queue.popleft())


    queue = []

    queue.append(1)
    queue.append(2)
    queue.append(3)

    print('\nInitial queue')
    print(queue)
    queue.reverse()
    print(queue)

    print('\nElements removed from queue:')
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))