N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

result = 0

for i in range(3):
    pebble = i + 1
    score = 0
    for j in range(len(times)):
        a, b, c = times[j]
        if a == pebble:
            pebble = b
        elif b == pebble:
            pebble = a
        if pebble == c:
            score += 1
    result = max(result, score)

print(result)
