import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')



def orient(v, u, w):  return np.linalg.det(np.vstack((np.ones(3), np.vstack((v, u, w)).transpose())))


def read_convex_orign(src: str):

    with open(src) as file:

        data = file.readlines()
        return np.loadtxt(data[1:-1], dtype = int), np.loadtxt(data[-1:], dtype = int)


def find_tangent_point(conv, orig) -> np.ndarray:

    ind = speed = len(conv) // 2
    def get_pnt(ind: int) -> np.ndarray: return conv[ind % len(conv)]

    while True:

        if    orient(orig, get_pnt(ind), get_pnt(ind + 1)) <= 0: ind += speed
        elif  orient(orig, get_pnt(ind), get_pnt(ind - 1)) <= 0: ind -= speed
        else: return ind % len(conv)

        if speed > 1: speed //= 2


def display_tangent(src: str):

    conv, orig = read_convex_orign(src)
    tang = conv[find_tangent_point(conv, orig)]

    plt.scatter(conv[:, 0], conv[:, 1])
    for p1, p2 in zip(conv, conv[1:].tolist() + [conv[0]] ): plt.plot([p1[0], p2[0]], [p1[1], p2[1]], c = 'b')
    plt.scatter([tang[0]], [tang[1]], c = 'r')
    plt.scatter([orig[0]], [orig[1]], c = 'r')
    plt.show()