import math

X = int(input())

peak = 0

while True:
    if (peak + 1) ** 2 > X:
        break
    peak += 1

time, distance, left = peak * 2 - 1, peak ** 2, X - (peak ** 2)
time += math.ceil(left / peak)

print(time)
