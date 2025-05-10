from sortedcontainers import SortedSet 

n = int(input())
P, L = [], []
for _ in range(n):
    p, l = map(int, input().split())
    P.append(p)
    L.append(l)

m = int(input())
commands = []
for _ in range(m):
    cmd = input().split()
    if cmd[0] == "rc":
        commands.append((cmd[0], int(cmd[1])))
    else:
        commands.append((cmd[0], int(cmd[1]), int(cmd[2])))

s = SortedSet()

for i in range(n):
    s.add((L[i], P[i]))

for command in commands:
    if command[0] == 'rc':
        if command[1] == 1:
            print(s[-1][1])
        else:
            print(s[0][1])
    if command[0] == 'ad':
        s.add((command[2], command[1]))
    if command[0] == 'sv':
        s.remove((command[2], command[1]))
