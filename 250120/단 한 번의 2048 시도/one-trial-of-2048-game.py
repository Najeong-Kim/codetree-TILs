# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Write your code here!
dirs = ['L', 'R', 'U', 'D']
dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]

if dir == 'L' or dir == 'R':
    arr = []
    for i in range(4):
        prev = grid[i]
        next = []
        now = 0
        repeat = [3, 2, 1, 0] if dir == 'R' else [0, 1, 2, 3]
        for j in repeat:
            if prev[j] == 0:
                continue
            if now == prev[j]:
                next.append(now * 2)
                now = 0
            else:
                if now != 0:
                    next.append(now)
                now = prev[j]
        while len(next) < 4:
            if now != 0:
                next.append(now)
                now = 0
            else:
                next.append(0)
        if dir == 'R':
            next = reversed(next)
        arr.append(next)

if dir == 'U' or dir == 'D':
    arr = [[] for _ in range(4)]
    for i in range(4):
        prev = [grid[j][i] for j in range(4)]
        next = []
        now = 0
        repeat = [3, 2, 1, 0] if dir == 'D' else [0, 1, 2, 3]
        for j in repeat:
            if prev[j] == 0:
                continue
            if now == prev[j]:
                next.append(now * 2)
                now = 0
            else:
                if now != 0:
                    next.append(now)
                now = prev[j]
        while len(next) < 4:
            if now != 0:
                next.append(now)
                now = 0
            else:
                next.append(0)
        if dir == 'D':
            next.reverse()
        for j in range(4):
            arr[j].append(next[j])

for elem in arr:
    print(*elem)
