T = int(input())

dir, dx, dy = {'L': 0, 'R': 1, 'U': 2, 'D': 3}, [-1, 1, 0, 0], [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x <= 4000 and 0 <= y <= 4000

for _ in range(T):
    time = 0
    result = -1
    N = int(input())
    x, y, w, d = [], [], [], []

    for i in range(N):
        xi, yi, wi, di = input().split()
        nx, ny = (int(xi) + 1000) * 2, (int(yi) + 1000) * 2
        x.append(nx)
        y.append(ny)
        w.append(int(wi))
        d.append(di)

    while time <= 4000:
        time += 1
        check = {}

        for i in range(len(x)):
            if x[i] == None:
                continue
            di = dir[d[i]]
            cx, cy = x[i] + dx[di], y[i] + dy[di]
            if not in_range(cx, cy):
                x[i] = None
                continue
            if (cx, cy) in check:
                exist = check[(cx, cy)]
                if w[i] > w[exist] or (w[i] == w[exist] and i > exist):
                    check[(cx, cy)] = i
                    x[i] = cx
                    y[i] = cy
                    x[exist] = None
                else:
                    x[i] = None
                result = time
            else:
                check[(cx, cy)] = i
                x[i] = cx
                y[i] = cy

    print(result)
