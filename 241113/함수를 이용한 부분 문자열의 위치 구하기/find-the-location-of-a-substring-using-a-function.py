M = input()
N = input()

def find_position_of_substring(string, target):
    if len(string) < len(target):
        return -1
    index = -1
    for i in range(len(string) - len(target) + 1):
        if string[i:i+len(target)] == target:
            index = i
    return index

print(find_position_of_substring(M, N))