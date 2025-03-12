def solution(money):
    a = money//5500
    answer = [a,0]
    answer[1] = money - a*5500
    
    return answer