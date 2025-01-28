n, m, t = map(int, input().split())

dir, dx, dy = ['U', 'D', 'R', 'L'], [-1, 1, 0, 0], [0, 0, 1, -1]
change = [1, 0, 3, 2]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

r = []
c = []
d = []
w = []
num = []

for i in range(m):
    ri, ci, di, wi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    w.append(int(wi))
    num.append(i + 1)

for _ in range(t):
    board = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(len(r)):
        nd = dir.index(d[i])
        nr, nc = r[i] - 1 + dx[nd], c[i] - 1 + dy[nd]
        if in_range(nr, nc):
            board[nr][nc].append((d[i], w[i], num[i]))
        else:
            board[r[i] - 1][c[i] - 1].append((dir[change[nd]], w[i], num[i]))
    nr, nc, nd, nw, nnum = [], [], [], [], []
    for i in range(n):
        for j in range(n):
            arr = board[i][j]
            if len(arr) == 0:
                continue
            elif len(arr) == 1:
                nr.append(i + 1)
                nc.append(j + 1)
                nd.append(arr[0][0])
                nw.append(arr[0][1])
                nnum.append(arr[0][2])
            else:
                arr.sort(lambda x: x[2])
                nr.append(i + 1)
                nc.append(j + 1)
                nd.append(arr[-1][0])
                weight = 0
                for k in arr:
                    weight += k[1]
                nw.append(weight)
                nnum.append(arr[-1][2])
    r, c, d, w, num = nr, nc, nd, nw, nnum

max_weight = 0
for i in range(len(r)):
    max_weight = max(max_weight, w[i])
print(len(r), max_weight)