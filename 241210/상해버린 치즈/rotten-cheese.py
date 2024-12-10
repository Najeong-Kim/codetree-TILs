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
    extra = 0
    is_spoiled = True
    for j in range(1, N + 1):
        eat = list(filter(lambda x: x[0] == j, eats[i]))
        if len(eat):
            min_eat_time = eat[0][1]
            for k in eat:
                min_eat_time = min(k[1], min_eat_time)
            if j in sicks:
                if sicks[j] > min_eat_time:
                    count += 1
                else:
                    is_spoiled = False
            else:
                extra += 1
        else:
            if j in sicks:
                is_spoiled = False
    if is_spoiled:
        result = max(result, count + extra)

print(result)