N, K = map(int, input().split())
arr = [''] * 10001

for _ in range(N):
    position, alphabet = input().split()
    arr[int(position)] = alphabet

max_num = 0

for i in range(len(arr) - K):
    score = 0
    for j in range(i, i + K + 1):
        if arr[j] == 'G':
            score += 1
        if arr[j] == 'H':
            score += 2
        max_num = max(score, max_num)

print(max_num)