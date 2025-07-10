def solution(number):
    return sum(map(lambda x: int(x), list(number)))%9