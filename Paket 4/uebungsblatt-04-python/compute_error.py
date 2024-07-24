import numpy as np


def compute_error(u, xh, uHat):
    N = len(xh)
    M = 100 * (N - 1) + 1
    xk = np.linspace(xh[0], xh[N - 1], M)
    yk = u(xk)
    zk = np.interp(xk, xh, uHat)
    return np.max(np.abs(yk - zk))
