def print_1_to_N(N):
    if (N == 0):
        return
    print_1_to_N(N - 1)
    print(N, end=" ")

def print_N_to_1(N):
    if (N == 0):
        return
    print(N, end=" ")
    print_N_to_1(N - 1)

N = int(input())
print_1_to_N(N)
print("")
print_N_to_1(N)