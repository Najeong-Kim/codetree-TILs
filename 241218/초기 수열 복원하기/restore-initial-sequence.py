N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    cur = [i + 1]
    index = 0
    is_answer = False
    while True:
        if index == len(arr):
            is_answer = True
            for elem in cur:
                print(elem, end=' ')
            break
        next_number = arr[index] - cur[-1]
        if next_number in cur or next_number < 1:
            break
        else:
            cur.append(next_number)
            index += 1
    if is_answer:
        break
