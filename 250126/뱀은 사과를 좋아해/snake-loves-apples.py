N, M, K = map(int, input().split())

x, y = [], []
for _ in range(M):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

d, p = [], []
for _ in range(K):
    di, pi = input().split()
    d.append(di)
    p.append(int(pi))

# Write your code here!
snake_x, snake_y = [1], [1]
directions, dx, dy = ['U', 'D', 'R', 'L'], [-1, 1, 0, 0], [0, 0, 1, -1]

def in_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

time = 0
is_finished = False

for i in range(K):
    if is_finished:
        break
    now_d, now_p = d[i], p[i]
    direction = directions.index(now_d)
    for _ in range(now_p):
        if is_finished:
            break
        time += 1
        now_x, now_y = snake_x[0] + dx[direction], snake_y[0] + dy[direction]
        if not in_range(now_x, now_y):
            is_finished = True
            break
        for j in range(len(snake_x)):
            if snake_x[j] == now_x and snake_y[j] == now_y:
                is_finished = True
                break
        apple_index = -1
        for j in range(len(x)):
            if x[j] == now_x and y[j] == now_y:
                apple_index = j
                break
        if apple_index == -1:
            snake_x = [now_x] + snake_x[:-1]
            snake_y = [now_y] + snake_y[:-1]
        else:
            del x[apple_index]
            del y[apple_index]
            snake_x = [now_x] + snake_x
            snake_y = [now_y] + snake_y

print(time)