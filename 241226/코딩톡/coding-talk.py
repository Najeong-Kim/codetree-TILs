n, m, p = map(int, input().split())
messages = [list(input().split()) for _ in range(m)]
alphabet = 'ABCDEFJHIJKLMNOPQRSTUVWXYZ'
read = [False] * n

for i in range(m):
    c, u = messages[i]
    index = alphabet.find(c)
    if i >=  p - 1 or u == messages[p - 1][1]:
        read[index] = True

for i in range(n):
    if not read[i]:
        print(alphabet[i], end=' ')