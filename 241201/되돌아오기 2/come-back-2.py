path = input()

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0
d = 0
count = 0
is_return = False

for i in range(len(path)):
    command = path[i]
    count += 1
    if command == 'F':
        x, y = x + dx[d], y + dy[d]
        if x == 0 and y == 0:
            print(count)
            is_return = True
            break
    if command == 'R':
        d = (d + 1) % 4
    if command == 'L':
        d = (d + 3) % 4

if not is_return:
    print(-1)