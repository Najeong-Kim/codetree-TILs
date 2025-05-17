N, Q = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

prefix_sum = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(3):
        if arr[i - 1] == j + 1:
            prefix_sum[i][j] = prefix_sum[i - 1][j] + 1
        else:
            prefix_sum[i][j] = prefix_sum[i - 1][j]

for i in range(Q):
    for j in range(3):
        print(prefix_sum[queries[i][1]][j] - prefix_sum[queries[i][0] - 1][j], end=' ')
    print()
