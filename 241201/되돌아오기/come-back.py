N = int(input())
mapper = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0
count = 0
is_return = False

for _ in range(N):
    d, c = input().split()
    d = mapper[d]
    c = int(c)
    for i in range(c):
        x, y = x + dx[d], y + dy[d]
        count += 1
        if x == 0 and y == 0:
            print(count)
            is_return = True
            break
    if is_return:
        break

if not is_return:
    print(-1)