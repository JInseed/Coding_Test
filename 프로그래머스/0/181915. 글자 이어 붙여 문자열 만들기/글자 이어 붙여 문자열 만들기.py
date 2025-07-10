def solution(my_string, index_list):
    return ''.join(my_string[i] for i in index_list)

# def solution(my_string, index_list):
#     return ''.join(map(lambda x: my_string[x], index_list))