N, K, P, T = map(int, input().split())
result = [0] * (N + 1)
shakes = [False] * 251
result[P] = K + 1

for i in range(T):
    t, x, y = map(int, input().split())
    shakes[t] = [x, y]

for shake in shakes:
    if not shake:
        continue
    x, y = shake[0], shake[1]
    x_count, y_count = result[x], result[y]
    if not x_count and not y_count:
        continue
    elif x_count > 1:
        result[x] -= 1
        result[y] = K + 1
    elif y_count > 1:
        result[y] -= 1
        result[x] = K + 1

for i in range(1, len(result)):
    if result[i]:
        print('1', end="")
    else:
        print('0', end="")