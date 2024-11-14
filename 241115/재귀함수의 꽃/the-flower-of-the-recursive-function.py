def flower(N):
    if N == 0:
        return
    print(N, end=" ")
    flower(N-1)
    print(N, end=" ")

N = int(input())
flower(N)