# BVP -> y' = 2y - 1, y(0) = 1
# So, f(t,y) = 2y - 1

import numpy as np
import matplotlib.pyplot as plt

h = 0.1
start = 0.0
end = 10.0
initial_t = 0.0
initial_y = 1.0

def f(x, y):
    return 2 * y - 1

def forward_euler(f, start, end, h, initial_t, initial_y):
    y = np.zeros(int((end - start) / h) + 1)
    y[0] = initial_y
    for i in range(1, y.shape[0] - 1):
        y[i] = y[i - 1] + h * f(h * i - start, y[i - 1])
    t = h * np.arange(0, y.shape[0]) + start
    return y, t

if __name__ == '__main__':
    y, t = forward_euler(f, start, end, h, initial_t, initial_y)

print "Solution array for step size = ", h, ":", y
print "Output Grid = ", t

plt.scatter(t, y)
plt.show()
