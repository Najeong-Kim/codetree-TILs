N, M = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))

count = 0

for i in range(len(A) - len(B) + 1):
    sub_A = sorted(A[i:i+len(B)])
    is_beautiful = True
    for j in range(len(B)):
        if sub_A[j] != B[j]:
            is_beautiful = False
            break
    if is_beautiful:
        count += 1

print(count)
