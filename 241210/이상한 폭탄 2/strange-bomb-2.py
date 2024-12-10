N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

max_num = -1
for i in range(N):
    for j in range(i + 1, min(N, i + 1 + K)):
        if bombs[i] == bombs[j]:
            max_num = max(max_num, bombs[i])

print(max_num)
