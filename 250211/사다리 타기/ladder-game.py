n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

edges.sort(lambda x: x[1])

init = [i for i in range(1, n + 1)]
check = [i for i in range(1, n + 1)]

for edge in edges:
    init[edge[0] - 1], init[edge[0]] = init[edge[0]], init[edge[0] - 1]

result = len(edges)

def run(index, count):
    global result
    global check

    if check == init:
        result = min(result, count)

    if index == n + 1:
        return
    
    run(index + 1, count)

    line = edges[index][0]
    check[line - 1], check[line] = check[line], check[line - 1]
    run(index + 1, count + 1)
    check[line - 1], check[line] = check[line], check[line - 1]

run(0, 0)
run(0, 1)
print(result)