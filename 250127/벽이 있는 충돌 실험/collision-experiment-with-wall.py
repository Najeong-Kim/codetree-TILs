T = int(input())

dir, dx, dy = ['U', 'D', 'R', 'L'], [-1, 1, 0, 0], [0, 0, 1, -1]
change = [1, 0, 3, 2]

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

for _ in range(T):
    N, M = map(int, input().split())
    x, y, d = [], [], []
    for _ in range(M):
        xi, yi, di = input().split()
        x.append(int(xi))
        y.append(int(yi))
        d.append(di)
    for _ in range(2 * N + 2):
        board = [[[] for _ in range(N)] for _ in range(N)]
        for i in range(len(x)):
            nd = dir.index(d[i])
            nx, ny = x[i] - 1 + dx[nd], y[i] - 1 + dy[nd]
            if in_range(nx, ny, N):
                board[nx][ny].append(d[i])
            else:
                board[x[i] - 1][y[i] - 1].append(dir[change[nd]])
        nx, ny, nd = [], [], []
        for i in range(N):
            for j in range(N):
                if len(board[i][j]) == 1:
                    nx.append(i + 1)
                    ny.append(j + 1)
                    nd.append(board[i][j][0])
        x, y, d = nx, ny, nd
    
    print(len(x))
