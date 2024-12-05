N, M = map(int, input().split())
arr = []

for _ in range(N):
    words = input()
    sub_arr = []
    for word in words:
        sub_arr.append(word)
    arr.append(sub_arr)

result = 0

def find_lee(line):
    if line[0] == 'L' and line[1] == 'E' and line[2] == 'E':
        return 1
    return 0

for i in range(N):
    for j in range(M - 2):
        result += find_lee([arr[i][j], arr[i][j + 1], arr[i][j + 2]])
        result += find_lee([arr[i][j + 2], arr[i][j + 1], arr[i][j]])

for i in range(N - 2):
    for j in range(M):
        result += find_lee([arr[i][j], arr[i + 1][j], arr[i + 2][j]])
        result += find_lee([arr[i + 2][j], arr[i + 1][j], arr[i][j]])

for i in range(N - 2):
    for j in range(M - 2):
        result += find_lee([arr[i][j], arr[i + 1][j + 1], arr[i + 2][j + 2]])
        result += find_lee([arr[i + 2][j + 2], arr[i + 1][j + 1], arr[i][j]])

for i in range(N - 2):
    for j in range(2, M):
        result += find_lee([arr[i][j], arr[i + 1][j - 1], arr[i + 2][j - 2]])
        result += find_lee([arr[i + 2][j - 2], arr[i + 1][j - 1], arr[i][j]])

print(result)
