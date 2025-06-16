n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(lambda x: x[1])

finish = 0
result = 0
for meeting in meetings:
    start, end = meeting
    if finish <= start:
        result += 1
        finish = end

print(result)