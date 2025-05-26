n = int(input())
numbers = [int(input()) for _ in range(n)]

arr = [0]
for i in range(n):
    arr.append(arr[-1] + numbers[i])

dict = {}
for i in range(len(arr)):
    rest = arr[i] % 7
    if rest in dict:
        dict[rest].append(i)
    else:
        dict[rest] = [i]

result = 0
for i in range(7):
    if i not in dict or len(dict[i]) == 1:
        continue
    result = max(result, dict[i][-1] - dict[i][0])

print(result)