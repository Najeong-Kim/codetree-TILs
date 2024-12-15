N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

for i in range(11):
    for j in range(11):
        for k in range(11):
            for a in range(2):
                for b in range(2):
                    for c in range(2):
                        is_possible = True
                        for elem in arr:
                            if elem[a] != i and elem[b] != j and elem[c] != k:
                                is_possible = False
                                break
                        if is_possible:
                            result = 1

print(result)
