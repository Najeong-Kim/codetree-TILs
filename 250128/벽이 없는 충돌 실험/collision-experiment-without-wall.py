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

    while True:
        is_finish = True
        for i in range(len(x)):
            if -1000 <= x[i] <= 1000 and -1000 <= y[i] <= 1000:
                is_finish = False
                break
        if is_finish:
            break
        time += 1

        check = {}

        for i in range(len(x)):
            di = dir.index(d[i])
            x[i], y[i] = x[i] + dx[di] * 0.5, y[i] + dy[di] * 0.5
            if (x[i], y[i]) in check:
                check[(x[i], y[i])].append((w[i], d[i], num[i]))
            else:
                check[(x[i], y[i])] = [(w[i], d[i], num[i])]
        for i in check:
            if len(check[i]) >= 2:
                check[i].sort(lambda x: (x[0], x[2]))
                check[i] = [check[i][-1]]
                result = time
        nx, ny, nw, nd, nnum = [], [], [], [], []
        for i in check:
            nx.append(i[0])
            ny.append(i[1])
            nw.append(check[i][0][0])
            nd.append(check[i][0][1])
            nnum.append(check[i][0][2])
        x, y, w, d, num = nx, ny, nw, nd, nnum
    
    print(result)