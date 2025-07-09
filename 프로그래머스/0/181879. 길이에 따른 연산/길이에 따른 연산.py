def solution(num_list):
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        answer = 1
        for i in num_list:
            answer *= i 
    return answer

# from math import prod
# def solution(num_list):
#     return sum(num_list) if len(num_list)>=11 else prod(num_list)