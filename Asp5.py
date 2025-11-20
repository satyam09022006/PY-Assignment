t = int(input())

for _ in range(t):
    a, b = input().split()

    a = int(a[::-1])
    b = int(b[::-1])

    s = a + b
    s = int(str(s)[::-1])

    print(s)