boards = [list(map(int, input().split())) for _ in range(19)]

result = 0
x, y = 0, 0
has_won = False

def won(line):
    if all(stone == 1 for stone in line):
        return 1
    if all(stone == 2 for stone in line):
        return 2
    return 0

for i in range(19):
    if has_won:
        break
    for j in range(19 - 4):
        result = won([boards[i][j], boards[i][j + 1], boards[i][j + 2], boards[i][j + 3], boards[i][j + 4]])
        if result:
            x, y = i + 1, j + 3
            has_won = True
            break

for i in range(19 - 4):
    if has_won:
        break
    for j in range(19):
        result = won([boards[i][j], boards[i + 1][j], boards[i + 2][j], boards[i + 3][j], boards[i + 4][j]])
        if result:
            x, y = i + 3, j + 1
            has_won = True
            break

for i in range(19 - 4):
    if has_won:
        break
    for j in range(19 - 4):
        result = won([boards[i][j], boards[i + 1][j + 1], boards[i + 2][j + 2], boards[i + 3][j + 3], boards[i + 4][j + 4]])
        if result:
            x, y = i + 3, j + 3
            has_won = True
            break

for i in range(19 - 4):
    if has_won:
        break
    for j in range(4, 19):
        result = won([boards[i][j], boards[i + 1][j - 1], boards[i + 2][j - 2], boards[i + 3][j - 3], boards[i + 4][j - 4]])
        if result:
            x, y = i + 3, j - 1
            has_won = True
            break

print(result)
if result:
    print(x, y)
