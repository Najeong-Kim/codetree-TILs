T = int(input())

dir, dx, dy = ['L', 'R', 'U', 'D'], [-1, 1, 0, 0], [0, 0, 1, -1]

for _ in range(T):
    time = 0
    result = -1
    N = int(input())
    x, y, w, d, num = [], [], [], [], []

    for i in range(N):
        xi, yi, wi, di = input().split()
        x.append(int(xi))
        y.append(int(yi))
        w.append(int(wi))
        d.append(di)
        num.append(i + 1)

    while time <= 4000:
        time += 1

        check = {}

        for i in range(len(x)):
            di = dir.index(d[i])
            x[i], y[i] = x[i] + dx[di] * 0.5, y[i] + dy[di] * 0.5
            now = (w[i], d[i], num[i])
            if (x[i], y[i]) in check:
                exist = check[(x[i], y[i])]
                if now[0] > exist[0] or (now[0] == exist[0] and now[2] > exist[2]):
                    check[(x[i], y[i])] = now
                result = time
            else:
                check[(x[i], y[i])] = now
        nx, ny, nw, nd, nnum = [], [], [], [], []
        for i in check:
            nx.append(i[0])
            ny.append(i[1])
            nw.append(check[i][0])
            nd.append(check[i][1])
            nnum.append(check[i][2])
        x, y, w, d, num = nx, ny, nw, nd, nnum
    
    print(result)