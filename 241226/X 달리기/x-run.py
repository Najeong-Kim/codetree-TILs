X = int(input())

result = 10000

def run(speed, time, distance, increase):
    global result
    if distance >= X:
        if speed == 1:
            result = min(result, time)
        return
    if increase == 1:
        speed += 1
    elif increase == -1:
        speed = max(speed - 1, 1)
    time += 1
    distance += speed
    run(speed, time, distance, 1)
    run(speed, time, distance, 0)
    run(speed, time, distance, -1)

run(0, 0, 0, 1)

print(result)
