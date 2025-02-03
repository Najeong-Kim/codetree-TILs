from collections import deque

N = int(input())

step = [10 ** 6] * (10 ** 6 + 1)
visited = [False] * (10 ** 6 + 1)
deq = deque()
visited[N] = True
deq.append(N)
step[N] = 0

while len(deq):
    n = deq.popleft()
    if n == 1:
        print(step[n])
        break
    if n + 1 == 1 or n - 1 == 1 or (n % 3 == 0 and n // 3 == 1) or (n % 2 == 0 and n // 2 == 1):
        print(step[n] + 1)
        break
    if n + 1 < N:
        step[n + 1] = min(step[n + 1], step[n] + 1)
        deq.append(n + 1)
    if n - 1 >= 0:
        step[n - 1] = min(step[n - 1], step[n] + 1)
        deq.append(n - 1)
    if n % 3 == 0:
        step[n // 3] = min(step[n // 3], step[n] + 1)
        deq.append(n // 3)
    if n % 2 == 0:
        step[n // 2] = min(step[n // 2], step[n] + 1)
        deq.append(n // 2)
