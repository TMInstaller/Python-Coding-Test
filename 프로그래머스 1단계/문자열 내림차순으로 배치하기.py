# 유의사항: sort()는 문자열 상태에서 실행할 수 없다
def solution(s):
    answer = ''
    s = list(s)
    s.sort()
    s.reverse()
    for i in s:
        answer = answer + i
    return answer
