N = int(input())
arr = [-1] * 11

count = 0

for i in range(N):
    number, position = map(int, input().split())
    if arr[number] == -1:
        arr[number] = position
    elif arr[number] != position:
        count += 1
        arr[number] = position

print(count)