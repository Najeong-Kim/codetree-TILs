n = int(input())
arr = [""] * 20000
position = 10000

for _ in range(n):
    x, direction = input().split()
    if direction == 'L':
        for i in range(int(x)):
            position -= 1
            if arr[position] == 'g':
                continue
            if len(arr[position]) == 0 or arr[position][-1] == 'b':
                arr[position] += 'w'
            if len(arr[position]) == 4:
                arr[position] = 'g'
    else:
        for i in range(int(x)):
            if arr[position] == 'g':
                continue
            if len(arr[position]) == 0 or arr[position][-1] == 'w':
                arr[position] += 'b'
            if len(arr[position]) == 4:
                arr[position] = 'g'
            position += 1

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
