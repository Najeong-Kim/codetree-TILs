N, M, K = map(int, input().split())

penalty_list = [0] * (N + 1)

has_penalty = False

for _ in range(M):
    student = int(input())
    penalty_list[student] += 1
    if penalty_list[student] >= K:
        print(student)
        has_penalty = True
        break

if not has_penalty:
    print(-1)