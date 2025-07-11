def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        if numLog[i+1] - numLog[i] == 1:
            answer+='w'
        elif numLog[i+1] - numLog[i] == -1:
            answer+='s'
        elif numLog[i+1] - numLog[i] == 10:
            answer+='d'
        else:
            answer+='a'
    return answer

# def solution(log):
#     res=''
#     joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
#     for i in range(1,len(log)):
#         res+=joystick[log[i]-log[i-1]]
#     return res