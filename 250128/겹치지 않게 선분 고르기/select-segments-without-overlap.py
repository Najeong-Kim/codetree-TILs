n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

lines = []
result = 0

def run(i):
    global lines
    global result

    if i >= n:
        result = max(result, len(lines))
        return
    
    is_collapsed = False
    for line in lines:
        if not (x1[line] > x2[i] or x2[line] < x1[i]):
            is_collapsed = True
            break
    if is_collapsed:
        run(i + 1)
    else:
        lines.append(i)
        run(i + 1)
        lines.pop()

run(0)
print(result)