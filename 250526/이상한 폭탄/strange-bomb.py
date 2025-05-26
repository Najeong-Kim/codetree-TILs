n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

bomb = {}

for i in range(len(arr)):
    if arr[i] in bomb:
        bomb[arr[i]].append(i)
    else:
        bomb[arr[i]] = [i]

result = -1

for i in range(1000001, 0, -1):
    if i not in bomb:
        continue
    for j in range(1, len(bomb[i])):
        if bomb[i][j] - bomb[i][j - 1] <= k:
            result = i
            break
    if result != -1:
        break

print(result)
