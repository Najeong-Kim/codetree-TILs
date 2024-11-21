n = int(input())
arr = [0] * 2000
position = 1000

for _ in range(n):
    x, direction = input().split()
    if direction == 'L':
        for i in range(int(x)):
            position -= 1
            arr[position] += 1
    else:
        for i in range(int(x)):
            arr[position] += 1
            position += 1

result = 0

for i in arr:
    if i >= 2:
        result += 1

print(result)
