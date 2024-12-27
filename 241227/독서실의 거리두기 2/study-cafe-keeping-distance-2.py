import math

N = int(input())
seats = list(input())

def get_distance(seats, isMax = True):
    start, end = -1, -1
    now = 0 if seats[0] == '1' else 1
    distance = 0 if isMax else 1000
    for i in range(1, len(seats)):
        now += 1
        if seats[i] == '1':
            if isMax and now > distance:
                start, end = i - now, i
                distance = now
            elif not isMax and now < distance and i - now != -1:
                distance = now
            now = 0
    if isMax and now > distance:
        start, end = len(seats) - now - 1, len(seats)
        distance = now
    return start, end, distance

start, end, distance = get_distance(seats)
_, _, existed = get_distance(seats,False)

if start == -1 or end == len(seats):
    print(min(distance - 1, existed))
else:
    print(min(math.floor(distance / 2), existed))
