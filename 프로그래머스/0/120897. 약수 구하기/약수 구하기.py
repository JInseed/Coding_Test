def solution(n):
    answer = []
    for i in range(1, int(n**(0.5))+1):
        if (n%i == 0):
            answer+=list(set([i, n//i]))
    return sorted(answer)