n = int(input())
word = input()

C = [0] * n
C[0] = 1 if word[0] == 'C' else 0
for i in range(1, n):
    C[i] = C[i - 1]
    if word[i] == 'C':
        C[i] += 1

W = [0] * n
W[-1] = 1 if word[-1] == 'W' else 0
for i in range(n - 2, -1, -1):
    W[i] = W[i + 1]
    if word[i] == 'W':
        W[i] += 1

count = 0
for i in range(1, n - 1):
    if word[i] == 'O':
        count += C[i - 1] * W[i + 1]

print(count)