import numpy as np
import time

pwr = int(input("Enter the power value: "))

n = 2 ** pwr

rows_x = n #rows in matrix x
cols_x = n #rows in matrix y

entries = np.random.randint(255, size=(n*n))

matrix_x = np.array(entries).reshape(rows_x, cols_x)
x_transpose = matrix_x.transpose()

rows_y = n
cols_y = n

entries = np.random.randint(255, size=(n*n))

matrix_y = np.array(entries).reshape(rows_y, cols_y)
y_transpose = matrix_y.transpose()

ts = time.time() #recording the start time

res = matrix_x.dot(matrix_x) + matrix_x.dot(x_transpose) + (matrix_y.dot(matrix_y)) * 4

te = time.time()

print("time in serial: ", te-ts)
