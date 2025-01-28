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
            if (x[i], y[i]) in check:
                exist = check[(x[i], y[i])]
                if w[i] > w[exist] or (w[i] == w[exist] and num[i] > num[exist]):
                    check[(x[i], y[i])] = i
                result = time
            else:
                check[(x[i], y[i])] = i
        nx, ny, nw, nd, nnum = [], [], [], [], []
        for i in check:
            nx.append(i[0])
            ny.append(i[1])
            nw.append(w[check[i]])
            nd.append(d[check[i]])
            nnum.append(num[check[i]])
        x, y, w, d, num = nx, ny, nw, nd, nnum
    
    print(result)
