arr = [list(input()) for _ in range(3)]

count = 0

def is_won(line):
    if line[0] == line[1] or line[1] == line[2] or line[2] == line[0]:
        if not line[0] == line[1] == line[2]:
            return True
    return False

for i in range(3):
    line = arr[i]
    if is_won(line):
        count += 1

for i in range(3):
    line = []
    for j in range(3):
        line.append(arr[j][i])
    if is_won(line):
        count += 1

for i in range(1):
    line = []
    for j in range(3):
        line.append(arr[j][j])
    if is_won(line):
        count += 1

for i in range(1):
    line = []
    for j in range(3):
        line.append(arr[j][2 - j])
    if is_won(line):
        count += 1

print(count)