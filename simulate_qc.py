import numpy as np

def simulate_qc(time_array, y_road, ms, mu, kt, k, b, c):
    vs = np.zeros(len(time_array), float)
    vu = np.zeros(len(time_array), float)
    ys = np.zeros(len(time_array), float)
    yu = np.zeros(len(time_array), float)
    #initial conditions
    vs[0] = 0
    vu[0] = 0
    ys[0] = 0
    yu[0] = 0

    for i in range(1, len(time_array)):
        delta = time_array[i] - time_array[i - 1]
        ft = c * (vs[i - 1] - vu[i - 1]) + k * (ys[i - 1] - yu[i - 1])
        ht = ft - kt * yu[i - 1] + kt * y_road[i - 1]
        ys[i] = ys[i - 1] + vs[i - 1] * delta
        yu[i] = yu[i - 1] + vu[i - 1] * delta
        vs[i] = vs[i - 1] + ((-1 * (mu + b) * ft + b * ht) / ((ms * mu) + (ms + mu) * b)) * delta
        vu[i] = vu[i - 1] + ((-1 * b * ft + (ms + b) * ht) / ((ms * mu) + (ms + mu) * b)) * delta
        print(i)

    return vs, vu, ys, yu


# The function is only tested until the return statement in code to test the simulation function.
time_array = np.arange(0, 2, 0.001) # parameters for simulation
y_road = np.arange(1, 1001, 0.5)
ms = 250
mu = 35
kt = 150e3
k = 1000
b = 1500
c = 5000
vs, vu, ys, yu = simulate_qc(time_array, y_road, ms, mu, kt, k, b, c)
