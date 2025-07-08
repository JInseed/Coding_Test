def solution(my_string):
    answer = []
    for i in my_string:
        try: 
            answer.append(int(i))
        except:
            pass
        
    return sorted(answer)

# 다른 풀이는 isdigit 이라는 함수로 판별하거나, 정규표현식 씀