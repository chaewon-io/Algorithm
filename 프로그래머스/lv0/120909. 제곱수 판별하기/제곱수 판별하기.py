def solution(n):
    i = n ** (1/2)
    if i % 1 == 0:
        return 1
    else:
        return 2