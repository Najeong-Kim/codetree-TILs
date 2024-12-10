N, M, D, S = map(int, input().split())
eats = [[] for _ in range(M)]
sicks = {}

for _ in range(D):
    p, m, t = map(int, input().split())
    eats[m - 1].append([p, t])

for _ in range(S):
    p, t = map(int, input().split())
    sicks[p] = t

result = 0

for i in range(M):
    count = 0
    for j in range(1, N + 1):
        eat = list(filter(lambda x: x[0] == j, eats[i]))
        if len(eat):
            eat_time = eat[0][1]
            if j in sicks:
                if sicks[j] > eat_time:
                    count += 1
            else:
                count += 1
    result = max(result, count)

print(result)