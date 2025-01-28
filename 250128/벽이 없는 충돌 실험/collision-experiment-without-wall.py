T = int(input())

dir, dx, dy = {'L': 0, 'R': 1, 'U': 2, 'D': 3}, [-1, 1, 0, 0], [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x <= 4000 and 0 <= y <= 4000

for _ in range(T):
    time = 0
    result = -1
    N = int(input())
    x, y, w, d = [], [], [], []

    check = [[[] for _ in range(4001)] for _ in range(4001)]

    for i in range(N):
        xi, yi, wi, di = input().split()
        nx, ny = (int(xi) + 1000) * 2, (int(yi) + 1000) * 2
        x.append(nx)
        y.append(ny)
        w.append(int(wi))
        d.append(di)
        check[nx][ny].append(i)

    while time <= 4000:
        time += 1

        for i in range(len(x)):
            if x[i] == None:
                continue
            di = dir[d[i]]
            cx, cy = x[i] + dx[di], y[i] + dy[di]
            check[x[i]][y[i]].remove(i)
            if not in_range(cx, cy):
                x[i] = None
                continue
            now = list(filter(lambda x: x < i, check[cx][cy]))
            if len(now):
                exist = now[0]
                if w[i] > w[exist] or (w[i] == w[exist] and i > exist):
                    check[cx][cy][check[cx][cy].index(exist)] = i
                    x[i] = cx
                    y[i] = cy
                    x[exist] = None
                else:
                    x[i] = None
                result = time
            else:
                check[cx][cy].append(i)
                x[i] = cx
                y[i] = cy

    print(result)
