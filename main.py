from utils import *
from time import perf_counter


if __name__ == '__main__':

    conv, orig = read_convex_orign('input/huge.txt')
    start = perf_counter()
    find_tangent_point(conv, orig)
    print(f'run time for input size of a 1000000 points" {perf_counter() - start} seconds')