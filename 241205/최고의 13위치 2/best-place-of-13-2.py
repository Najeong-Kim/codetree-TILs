N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_coins = 0

for i in range(N):
    for j in range(N - 2):
        for k in range(N):
            for l in range(N - 2):
                if i == k and not (j + 2 < l):
                    continue
                coins = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                max_coins = max(coins, max_coins)

print(max_coins)
