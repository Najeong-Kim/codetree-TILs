n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

dict = {}
for command in commands:
    if command[0] == 'add':
        dict[command[1]] = command[2]
    if command[0] == 'remove':
        dict.pop(command[1])
    if command[0] == 'find':
        if command[1] in dict:
            print(dict[command[1]])
        else:
            print('None')