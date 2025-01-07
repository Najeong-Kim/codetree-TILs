n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# # 가능한 직사각형 모서리
# 시작점
# -n, -n (왼쪽 남은 값 1부터)
# +m -m (아래 남은 값 1부터)
# +n, +n
# -m, +m
dx = [-1, 1, 1, -1]
dy = [-1, -1, 1, 1]

result = 0

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                now = 0
                position = [i, j]
                is_out = False
                for a in range(k):
                    position[0] = position[0] + dx[0]
                    position[1] = position[1] + dy[0]
                    if 0 <= position[0] < n and 0 <= position[1] < n:
                        now += grid[position[0]][position[1]]
                    else:
                        is_out = True
                        break
                for a in range(l):
                    position[0] = position[0] + dx[1]
                    position[1] = position[1] + dy[1]
                    if 0 <= position[0] < n and 0 <= position[1] < n:
                        now += grid[position[0]][position[1]]
                    else:
                        is_out = True
                        break
                for a in range(k):
                    position[0] = position[0] + dx[2]
                    position[1] = position[1] + dy[2]
                    if 0 <= position[0] < n and 0 <= position[1] < n:
                        now += grid[position[0]][position[1]]
                    else:
                        is_out = True
                        break
                for a in range(l):
                    position[0] = position[0] + dx[3]
                    position[1] = position[1] + dy[3]
                    if 0 <= position[0] < n and 0 <= position[1] < n:
                        now += grid[position[0]][position[1]]
                    else:
                        is_out = True
                        break
                if not is_out:
                    result = max(result, now)

print(result)
