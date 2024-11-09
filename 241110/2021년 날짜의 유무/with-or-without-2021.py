def is_valid_date_2021(M, D):
    if M == 1 and D <= 31:
        return 'Yes'
    if M == 2 and D <= 28:
        return 'Yes'
    if M == 3 and D <= 31:
        return 'Yes'
    if M == 4 and D <= 30:
        return 'Yes'
    if M == 5 and D <= 31:
        return 'Yes'
    if M == 6 and D <= 30:
        return 'Yes'
    if M == 7 and D <= 31:
        return 'Yes'
    if M == 8 and D <= 31:
        return 'Yes'
    if M == 9 and D <= 30:
        return 'Yes'
    if M == 10 and D <= 31:
        return 'Yes'
    if M == 11 and D <= 30:
        return 'Yes'
    if M == 12 and D <= 31:
        return 'Yes'
    return 'No'

M, D = map(int, input().split())
print(is_valid_date_2021(M, D))