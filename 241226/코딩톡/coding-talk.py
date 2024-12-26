n, m, p = map(int, input().split())
messages = [list(input().split()) for _ in range(m)]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
read = [False] * n

for i in range(m):
    c, u = messages[i]
    index = alphabet.find(c)
    if messages[p - 1][1] == '0':
        read[i] = True
    if i >=  p - 1 or u == messages[p - 1][1]:
        read[index] = True

for i in range(n):
    if not read[i]:
        print(alphabet[i], end=' ')