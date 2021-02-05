def solution(A):
    A.sort()
    small = 0

    if A[-1] <= 0 or len(A) == 0:
        return 1

    while A[0] <= 0:
        A.pop(0)

    for i in range(0, len(A)):
        if A[i] == small or A[i] == (small + 1):
            small = A[i]
        elif A[i] > (small + 1):
            return (small + 1)

    return (small + 1)
