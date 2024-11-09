def is_leap_year(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            return 'false'
        return 'true'
    return 'false'

input = int(input())
print(is_leap_year(input))