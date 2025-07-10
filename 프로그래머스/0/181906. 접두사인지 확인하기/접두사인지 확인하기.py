def solution(my_string, is_prefix):
    if len(is_prefix) < len(my_string):
        return 1 if my_string[:len(is_prefix)] == is_prefix else 0
    else:
        return 0