n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = 0
min_cost = 10 ** 9
for i in range(n - 1):
    min_cost = min(min_cost, cost[i])
    result += dist[i] * min_cost

print(result)