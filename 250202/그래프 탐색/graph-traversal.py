n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visited[1] = True
count = 0

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

def seek(node):
    global visited
    global count
    
    for elem in graph[node]:
        if visited[elem]:
            continue
        visited[elem] = True
        count += 1
        seek(elem)

seek(1)
print(count)