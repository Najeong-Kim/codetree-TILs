n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0
left = k
for coin in reversed(coins):
    count += left // coin
    left %= coin

print(count)