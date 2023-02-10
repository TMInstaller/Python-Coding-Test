# 유의사항 : count는 '1'을 찾으라고 해도 1을 찾을 수 있다
def solution(n):
    answer = n
    ncount = bin(n).count('1')
    new_ncount = -1
    while ncount != new_ncount:
        answer += 1
        new_ncount = bin(answer).count('1')
    return answer
