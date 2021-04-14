import sys


def gen(n):
    for i in range(n):
        yield i**2


# x = [1 ** 2 for i in range(100000)]
g = gen(100000)

# print(sys.getsizeof(x))
print(sys.getsizeof(g))
