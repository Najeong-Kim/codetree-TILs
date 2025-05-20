N = int(input())
B = [input() for _ in range(N)]

H = [0] * (N + 1)
S = [0] * (N + 1)
P = [0] * (N + 1)
H2 = [0] * (N + 1)
S2 = [0] * (N + 1)
P2 = [0] * (N + 1)

for i in range(N):
    if B[i] == 'S':
        H[i + 1] = H[i] + 1
        S[i + 1] = S[i]
        P[i + 1] = P[i]
    elif B[i] == 'P':
        H[i + 1] = H[i]
        S[i + 1] = S[i] + 1
        P[i + 1] = P[i]
    else:
        H[i + 1] = H[i]
        S[i + 1] = S[i]
        P[i + 1] = P[i] + 1

for i in range(N - 1, -1, -1):
    if B[i] == 'S':
        H2[i] = H2[i + 1] + 1
        S2[i] = S2[i + 1]
        P2[i] = P2[i + 1]
    elif B[i] == 'P':
        H2[i] = H2[i + 1]
        S2[i] = S2[i + 1] + 1
        P2[i] = P2[i + 1]
    else:
        H2[i] = H2[i + 1]
        S2[i] = S2[i + 1]
        P2[i] = P2[i + 1] + 1

result = 0
for i in range(N):
    result = max(result, H[i] + S[i + 1], H[i] + P[i + 1], S[i] + H[i + 1], S[i] + P[i + 1], P[i] + S[i + 1], P[i] + H[i + 1])

print(result)
