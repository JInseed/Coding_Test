def solution(array):
    array.sort()
    return array[int((len(array) - 1)/2)]
