def solution(sides):
    l = max(sides)
    sides.remove(l)
    if l >= sum(sides):
        return 2
    else:
        return 1
