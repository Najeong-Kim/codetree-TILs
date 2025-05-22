from collections import deque

N, K = map(int, input().split())
M = []
dir = []

for _ in range(N):
    m, d = input().split()
    M.append(int(m))
    dir.append(d)

queue = []
point = 0
for i in range(N):
    if dir[i] == 'R':
        queue.append((point, 1))
        queue.append((point + M[i], -1))
        point += M[i]
    else:
        queue.append((point, -1))
        queue.append((point - M[i], 1))
        point -= M[i]

queue.sort()
index = queue[0][0]
count = 0
result = 0

for i in range(len(queue)):
    cur_point, cur_value = queue[i]
    if cur_point == index:
        count += cur_value
    else:
        if count >= K:
            result += cur_point - index
        index = cur_point
        count += cur_value

print(result)
