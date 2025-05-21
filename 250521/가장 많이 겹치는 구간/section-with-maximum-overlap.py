n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

arr = [0] * 200001
for i in intervals:
    arr[i[0]] += 1
    arr[i[1]] -= 1

result = 0
value = 0
for i in range(200001):
    value += arr[i]
    result = max(result, value)

print(result)