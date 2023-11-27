#bj1074
#S1
N, r, c = map(int, input().split())

def zSearch(a, b, c, d, x, y):
    if b - a == 1:
        if x == a:
            if y == c:
                return 0
            else:
                return 1
        else:
            if y == c:
                return 2
            else:
                return 3

    mid_1 = (a + b - 1) // 2
    mid_2 = (c + d - 1) // 2
    size = ((b - a + 1) // 2) ** 2

    if x <= mid_1:
        if y <= mid_2:
            return zSearch(a, mid_1, c, mid_2, x, y)
        else:
            return size + zSearch(a, mid_1, mid_2 + 1, d, x, y)
    else:
        if y <= mid_2:
            return (2 * size) + zSearch(mid_1 + 1, b, c, mid_2, x, y)
        else:
            return (3 * size) + zSearch(mid_1 + 1, b, mid_2 + 1, d, x, y)


print(zSearch(0, 2 ** N - 1, 0, 2 ** N - 1, r, c))
