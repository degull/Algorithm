def solution(n):
    sum_even = sum(i for i in range(2, n+1, 2))
    return sum_even