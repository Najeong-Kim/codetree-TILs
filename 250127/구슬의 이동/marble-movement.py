n, m, t, k = map(int, input().split())

r, c, d, v = [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    v.append(int(vi))

dir, dx, dy = ['U', 'D', 'R', 'L'], [-1, 1, 0, 0], [0, 0, 1, -1]
change = [1, 0, 3, 2]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _ in range(t):
    board = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(len(r)):
        nd = dir.index(d[i])
        x, y = r[i] - 1, c[i] - 1
        for i in range(v[i]):
            nx, ny = x + dx[nd], y + dy[nd]
            if in_range(nx, ny):
                x, y = nx, ny
            else:
                nd = change[nd]
                x, y = x + dx[nd], y + dy[nd]
        board[x][y].append((dir[change[nd]], v[i]))
    for i in range(n):
        for j in range(n):
            board[i][j].sort(lambda x: x[1])
    
    nr, nc, nd, nv = [], [], [], []
    for i in range(n):
        for j in range(n):
            board[i][j].sort(lambda x: x[1])
            if len(board[i][j]) > k:
                board[i][j] = board[i][j][len(board[i][j]) - k:]
            for l in board[i][j]:
                nr.append(i + 1)
                nc.append(j + 1)
                nd.append(l[0])
                nv.append(l[1])
    r, c, d, v = nr, nc, nd, nv

print(len(r))
