
import matplotlib.pyplot as plt
import numpy as np
import cvxpy as cp
import time as time


# https://www.cvxpy.org/examples/basic/least_squares.html
def solve_by_cvxpy(mat, vec):
    start_time = time.time()
    x = cp.Variable(mat.shape[0])
    cost = cp.sum_squares(mat @ x - vec)
    prob = cp.Problem(cp.Minimize(cost))
    prob.solve()
    end_time = time.time()
    return end_time - start_time


# https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq
def solve_by_numpy(mat, vec):
    start_time = time.time()
    np.linalg.lstsq(mat, vec, rcond=None)
    end_time = time.time()
    return end_time - start_time


def draw(size, numpy_time, cvxpy_time):
    plt.plot(size, numpy_time, label='numpy')
    plt.plot(size, cvxpy_time, label='cvxpy')
    plt.ylabel('time')
    plt.xlabel('size')
    plt.legend()
    plt.show()


def check_diff():
    size, np_times, cp_times = [], [], []
    for s in range(10, 500):
        mat, vec = np.random.rand(s, s), np.random.rand(s)
        size.append(s)
        np_time = solve_by_numpy(mat, vec)
        np_times.append(np_time)
        cp_time = solve_by_cvxpy(mat, vec)
        cp_times.append(cp_time)
    draw(size, np_times, cp_times)


if __name__ == '__main__':
    check_diff()
    