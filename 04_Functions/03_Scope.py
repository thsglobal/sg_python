a, b = 1, 2
constant = 3.14
var = 1


def local_scope():
    x = 500 * constant
    y = 700 / constant
    return x, y, var * 2


z = local_scope()
print(z)
print(a, b)