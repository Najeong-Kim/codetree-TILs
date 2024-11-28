dir_num = 3
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

commands = input()

for i in range(len(commands)):
    command = commands[i]
    if command == 'R':
        dir_num = (dir_num + 1) % 4
    elif command == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif command == 'F':
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)