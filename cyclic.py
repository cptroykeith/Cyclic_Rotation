def solution(A, K):
    N = len(A)
    #B=A.copy()
    B = [None] * N
    for i in range(0,N):
        B[(i+K)%N] = A[i] = A[i]
    return B
    pass