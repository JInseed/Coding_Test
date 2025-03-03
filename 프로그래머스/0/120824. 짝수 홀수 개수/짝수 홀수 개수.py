def solution(num_list):
    even = 0
    odds = 0
    for i in num_list:
        if i%2 == 0:
            even+=1
        else:
            odds+=1
    return [even, odds]