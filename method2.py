import numpy as np
import time
import multiprocessing as mp

pwr = int(input("Enter the power value: "))

n = 2 ** pwr

rows_x = n
cols_x = n

entries = np.random.randint(255, size=(n*n))

matrix_x = np.array(entries).reshape(rows_x, cols_x)
x_transpose = matrix_x.transpose()

rows_y = n
cols_y = n

entries = np.random.randint(255, size=(n*n))

matrix_y = np.array(entries).reshape(rows_y, cols_y)
y_transpose = matrix_y.transpose()


def res(x, x_t, y):
    return x.dot(x) + x.dot(x_t) + (y.dot(y)) * 4

ts = time.time() #recording the start time
pool = mp.Pool(processes=4)
results = [pool.apply(res, args=(matrix_x, x_transpose, matrix_y))]
pool.close()
te = time.time()

print("time in serial: ", te-ts)

