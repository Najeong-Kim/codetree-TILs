n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def shift(index, d):
    if d == 'L':
        temp = a[index][-1]
        for i in reversed(range(m - 1)):
            a[index][i + 1] = a[index][i]
        a[index][0] = temp
    else:
        temp = a[index][0]
        for i in range(m - 1):
            a[index][i] = a[index][i + 1]
        a[index][-1] = temp

def is_waved(i, d):
    if d == 'U' and i > 0:
        for j in range(m):
            if a[i][j] == a[i - 1][j]:
                return True
    if d == 'D' and i < n - 1:
        for j in range(m):
            if a[i][j] == a[i + 1][j]:
                return True
    return False

for wind in winds:
    i, d = wind
    up_index, down_index = i - 1, i - 1
    up, down = True, True
    while up or down:
        if up_index == down_index:
            shift(up_index, d)
        else:
            if up:
                shift(up_index, d)
            if down:
                shift(down_index, d)
        if not is_waved(up_index, 'U'):
            up = False
        else:
            up_index -= 1
        if not is_waved(down_index, 'D'):
            down = False
        else:
            down_index += 1
        if d == 'L':
            d = 'R'
        else:
            d = 'L'

for elem in a:
    print(*elem)
