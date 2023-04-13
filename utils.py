import numpy as np


def orient(v, u, w):  return np.linalg.det(np.vstack((np.ones(3), np.vstack((v, u, w)).transpose())))


def read_convex_orign(src: str):

    with open(src) as file:

        data = file.readlines()
        return np.loadtxt(data[1:-1], dtype = int), np.loadtxt(data[-1:], dtype = int)


def find_tangent_point(conv, orig) -> np.ndarray:

    start, end = 0, len(conv) - 1

    while start <= end:

        middle = (start + end) // 2

        if middle + 1 < len(conv) and orient(orig, conv[middle], conv[middle + 1]) <= 0: start = middle + 1; continue
        if middle - 1 <= 0 and orient(orig, conv[middle], conv[middle - 1]) <= 0: end = middle - 1; continue
        return conv[middle]

    return conv[start]