n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
front = [0] * n
front[0] = arr[0]
back = [0] * n
back[-1] = arr[-1]
for i in range(1, n):
    front[i] = max(front[i - 1], arr[i])
for i in range(n - 2, -1, -1):
    back[i] = max(back[i + 1], arr[i])

for query in queries:
    start, end = query
    print(max(front[start - 2], back[end]))