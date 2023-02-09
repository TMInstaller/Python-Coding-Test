# 유의사항 : 문자열을 split으로 나누면 배열 형태로 나눠진다
def solution(s):
    answer = ''
    num = s.split(' ')
    n = []
    for i in num:
        n.append(int(i))
    n.sort()
    answer = answer + str(min(n))
    answer = answer + ' '
    answer = answer + str(max(n))
    return answer
