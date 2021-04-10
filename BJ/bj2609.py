n, m = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(n, m))
print(n * m // gcd(n, m))
