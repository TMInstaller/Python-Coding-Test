def solution(array, n):
    answer = 0
    while n in array:
        answer += 1
        array.pop(array.index(n))
    return answer
