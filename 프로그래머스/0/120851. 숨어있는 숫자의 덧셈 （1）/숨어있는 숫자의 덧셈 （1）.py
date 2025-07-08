def solution(my_string):
    answer = []
    for i in my_string:
        try:
            answer.append(int(i))
        except:
            pass
    return sum(answer)

# def solution(my_string):
#     return sum(int(i) for i in my_string if i.isdigit())