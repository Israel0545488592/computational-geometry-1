import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')



def orient(v, u, w):  return np.linalg.det(np.vstack((np.ones(3), np.vstack((v, u, w)).transpose())))


def read_convex_orign(src: str):

    with open(src) as file:

        data = file.readlines()
        return np.loadtxt(data[1:-1], dtype = int), np.loadtxt(data[-1:], dtype = int)


def find_tangent_point(conv, orig) -> np.ndarray:

    start, end = 0, len(conv) - 1

    while start <= end:

        middle = (start + end) // 2

        if orient(orig, conv[middle], conv[(middle + 1) % len(conv)]) <= 0: start = middle + 1; continue
        if orient(orig, conv[middle], conv[(middle - 1) % len(conv)]) <= 0: end = middle - 1; continue
        return middle

    return start


def display_tangent(src: str):

    conv, orig = read_convex_orign(src)
    tang = conv[find_tangent_point(conv, orig)]

    plt.scatter(conv[:, 0], conv[:, 1])
    for p1, p2 in zip(conv, conv[1:].tolist() + [conv[0]] ): plt.plot([p1[0], p2[0]], [p1[1], p2[1]], c = 'b')
    plt.scatter([tang[0]], [tang[1]], c = 'r')
    plt.scatter([orig[0]], [orig[1]], c = 'r')
    plt.show()