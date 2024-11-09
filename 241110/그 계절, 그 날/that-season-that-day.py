def is_leap_year(Y):
    if Y % 100 == 0 and Y % 400 != 0:
        return False
    if Y % 4 == 0:
        return True
    return False

def is_exist(Y, M, D):
    if M == 1 and D <= 31:
        return True
    if M == 2:
        if is_leap_year(Y):
            if D <= 29:
                return True
        else:
            if D <= 28:
                return True
    if M == 3 and D <= 31:
        return True
    if M == 4 and D <= 30:
        return True
    if M == 5 and D <= 31:
        return True
    if M == 6 and D <= 30:
        return True
    if M == 7 and D <= 31:
        return True
    if M == 8 and D <= 31:
        return True
    if M == 9 and D <= 30:
        return True
    if M == 10 and D <= 31:
        return True
    if M == 11 and D <= 30:
        return True
    if M == 12 and D <= 31:
        return True
    return False

def get_season(Y, M, D):
    if is_exist(Y, M, D):
        if M == 3 or M == 4 or M == 5:
            return 'Spring'
        if M == 6 or M == 7 or M == 8:
            return 'Summer'
        if M == 9 or M == 10 or M == 11:
            return 'Fall'
        if M == 12 or M == 1 or M == 2:
            return 'Winter'
    else:
        return -1

Y, M, D = map(int, input().split())
print(get_season(Y, M, D))