if __name__ == '__main__':

    import math
    M, N = map(int,input().split())
    if M == 1 and N == 1:
        print(0)
    else:
        print(int(M * N) // 2) 