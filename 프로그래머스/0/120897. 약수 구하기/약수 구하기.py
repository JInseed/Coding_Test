def solution(n):
    answer = []
    for i in range(1, int(n**(1/2))+1):
        if (n%i == 0):
            if (i != n//i):
                answer+=[i, n//i]
            else:
                answer.append(i)
    return sorted(answer)