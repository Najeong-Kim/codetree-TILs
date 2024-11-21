n = int(input())
arr = [""] * 200000
position = 100000

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'L':
        for i in range(position, position - x, -1):
            if arr[i] == 'g':
                continue
            arr[i] += 'w'
            if arr[i].count('w') >= 2 and arr[i].count('b') >= 2:
                arr[i] = 'g'
        position -= x - 1
    else:
        for i in range(position, position + x):
            if arr[i] == 'g':
                continue
            arr[i] += 'b'
            if arr[i].count('w') >= 2 and arr[i].count('b') >= 2:
                arr[i] = 'g'
        position += x - 1

white = 0
black = 0
gray = 0

for tile in arr:
    if len(tile) == 0:
        continue
    if tile[-1] == 'w':
        white += 1
    elif tile[-1] == 'b':
        black += 1
    elif tile == 'g':
        gray += 1


print(white, black, gray)
