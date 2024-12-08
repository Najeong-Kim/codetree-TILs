N = int(input())
B = []

for _ in range(N):
    asked, one, two = map(int, input().split())
    a, b, c = asked // 100, asked % 100 // 10, asked % 10
    B.append([[a, b, c], one, two])

def check_count(answer, index, asked):
    if answer == asked[index]:
        return '1'
    elif answer == asked[(index + 1) % 3] or answer == asked[(index + 2) % 3]:
        return '2'

count = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            answers = [i, j, k]
            is_possible = True
            for b in B:
                asked, one, two = b
                asked_count = {
                    '1': 0,
                    '2': 0
                }

                for index, answer in enumerate(answers):
                    check = check_count(answer, index, asked)
                    if check:
                        asked_count[check] += 1
                if asked_count['1'] != one or asked_count['2'] != two:
                    is_possible = False
                    break
            if is_possible:
                count += 1

print(count)
