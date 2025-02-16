def solution(babbling):
    answer = 0
    talk = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for say in talk:
            if say in word:
                word = word.replace(say, '*')
        if all(char == '*' for char in word):
            
            answer += 1

    return answer