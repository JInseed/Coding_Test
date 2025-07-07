def solution(hp):
    a = [hp//5, hp%5//3, hp%5%3]
    print(a)
    return sum(a)