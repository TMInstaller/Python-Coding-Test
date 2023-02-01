# 유의사항: 정수와 정수가 아닌 수를 활용하려면 끝까지 숫자가 어떤 형태인 지 주시하라
def solution(s):
    answer = ''
    count = len(s)/2
    if int(count) == count:
        answer = s[int(count)-1] + s[int(count)]
    else:
        answer = s[int(count)]
    return answer
