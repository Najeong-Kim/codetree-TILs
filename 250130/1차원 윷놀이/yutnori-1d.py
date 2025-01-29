n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

turn = 0
status = [1] * k
result = 0

def run():
    global turn
    global status
    global result

    if turn == n:
        count = 0
        for i in range(k):
            if status[i] >= m:
                count += 1
        result = max(result, count)
        return
    for i in range(k):
        status[i] += nums[turn]
        turn += 1
        run()
        turn -= 1
        status[i] -= nums[turn]

run()
print(result)
    