A = input()

back = [0] * len(A)
for i in range(len(A) - 1, 0, -1):
    if A[i - 1] + A[i] == '))':
        back[i - 1] = back[i] + 1
    else:
        back[i - 1] = back[i]

result = 0
for i in range(len(A) - 2):
    if A[i] + A[i + 1] == '((':
        result += back[i + 2]

print(result)