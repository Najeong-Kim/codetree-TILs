n, k = map(int, input().split())
candy = []
for _ in range(n):
    c, p = map(int, input().split())
    candy.append((p, c))

candy.sort()

start = 0
end = 0
current_candy = candy[0][1]
result = candy[0][1]

while end != n - 1:
    if start == end and candy[end + 1][0] - candy[start][0] > 2 * k:
        start += 1
        end += 1
        current_candy = candy[end][1]
        result = max(result, current_candy)
    else:
        if candy[end + 1][0] - candy[start][0] <= 2 * k:
            end += 1
            current_candy += candy[end][1]
            result = max(result, current_candy)
        else:
            start += 1
            current_candy -= candy[start][1]

print(result)
