

lock = [[1,1,1], [1,1,0], [1,0,1]]
key = [[0,0,0], [1,0,0], [0,1,1]]

print(lock[:])

a = lock[:][:]

lock[0][0] = 100

print(a)
