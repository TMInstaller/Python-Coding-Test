# 유의사항: 예외사항에 대해 넘어가지 말 것
def solution(a, b):
    if b < a:
        answer = a
        a = b
        b = answer
    answer = 0
    for i in range(a, b+1):
        answer = answer + i
    return answer
