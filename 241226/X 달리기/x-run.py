X = int(input())

result = 10000

for i in range(X):
    increase = True
    speed = 0
    time = 0
    distance = 0
    while True:
        if distance >= X:
            if speed == 1:
                result = min(result, time)
            break
        if time == i:
            increase = False
        if increase:
            speed += 1
        else:
            speed = max(speed - 1, 1)
        time += 1
        distance += speed

print(result)
