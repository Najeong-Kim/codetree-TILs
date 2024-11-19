num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

first_day = sum(num_of_days[:m1 + 1]) + d1
second_day = sum(num_of_days[:m2 + 1]) + d2

print(second_day - first_day)