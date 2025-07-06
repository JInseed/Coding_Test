def solution(my_string):
    a = list(my_string)
    answer = ''
    for i in a:
        if i not in ['a','i','o','e','u']:
            answer+=i
    return answer