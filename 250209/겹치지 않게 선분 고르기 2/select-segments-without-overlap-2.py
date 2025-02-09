n = int(input())
x_list = [list(map(int, input().split())) for _ in range(n)]
x_list.sort(lambda x: x[1])

count = 0
last = 0

for x in x_list:
    if last < x[0]:
        count += 1
        last = x[1]

print(count)
