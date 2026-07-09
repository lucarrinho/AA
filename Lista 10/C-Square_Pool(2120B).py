for _ in range(int(input())):
    n, s = map(int, input().split())
    acc = 0
    for _ in range(n):
        dx, dy, x, y = map(int, input().split())
        if (0-s)*(y-0)==(x-0)*(0-s):
            acc += 1
        elif (0-s)*(y-s)==(x-0)*(s-0):
            acc += 1
    print(acc)