n = int(input())
first_cards = list(map(int, input().split()))
second_cards = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        if first_cards[i] > second_cards[j]:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + second_cards[j])
        elif first_cards[i] < second_cards[j]:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

result = 0
for row in dp:
    result = max(result, max(row))

print(result)