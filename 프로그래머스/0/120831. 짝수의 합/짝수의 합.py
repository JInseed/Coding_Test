def solution(n):
    answer = [i for i in range(n+1) if i%2 == 0]
    return sum(answer)
# [i for i in range(2, n+1, 2)]