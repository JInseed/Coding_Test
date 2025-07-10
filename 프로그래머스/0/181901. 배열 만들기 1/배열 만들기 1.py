def solution(n, k):
    return list(range(k, k*(n//k)+1, k))