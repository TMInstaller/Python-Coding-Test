def solution(array):
    answer = []
    ans = max(array)
    answer.append(ans)
    answer.append(array.index(ans))
    return answer
