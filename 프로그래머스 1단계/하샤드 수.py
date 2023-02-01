# 유의사항 : 문제의 조건을 제대로 읽을 것
def solution(x):
    answer = False
    lx = list(str(x))
    s = 0
    for i in lx:
        s = s + int(i)
    if x % s == 0:
        answer = True
    return answer
