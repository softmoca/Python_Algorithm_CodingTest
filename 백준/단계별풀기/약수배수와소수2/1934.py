import sys
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcd(a, b):
    return a * b // gcd(a, b)

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(lcd(a, b))

