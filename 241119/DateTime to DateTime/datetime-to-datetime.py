a, b, c = map(int, input().split())

start = 11 * 60 + 11
end = (a - 11) * 24 * 60 + b * 60 + c

if end - start < 0:
    print(-1)
else:
    print(end - start)