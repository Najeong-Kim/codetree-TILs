n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
l = [0]
r = [0]

for i in range(n - 1):
    l.append(l[-1] + abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i]))
    r.append(r[-1] + abs(x[n - 1 - i] - x[n - 1 - i - 1]) + abs(y[n - 1 - i] - y[n - 1 - i - 1]))

r.reverse()

result = 10 ** 9
for i in range(1, n - 1):
    dist = abs(x[i - 1] - x[i + 1]) + abs(y[i - 1] - y[i + 1])
    result = min(result, l[i - 1] + r[i + 1] + dist)

print(result)