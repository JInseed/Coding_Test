# def solution(cipher, code):
#     answer = cipher[code-1::code]
#     return answer

def solution(cipher, code):
    return ''.join(cipher[i] for i in range(code-1,len(cipher),code))