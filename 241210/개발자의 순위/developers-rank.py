K, N = map(int, input().split())
rankings = [list(map(int, input().split())) for _ in range(K)]

count = 0

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            continue
        is_invariant = True
        for ranking in rankings:
            if ranking.index(a) < ranking.index(b):
                is_invariant = False
                break
        if is_invariant:
            count += 1

print(count)
