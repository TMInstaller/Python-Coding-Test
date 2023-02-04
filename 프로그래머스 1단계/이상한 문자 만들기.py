# 풀이
def solution(s):
    # 입력받은 문자열을 list 형태로 변경
    s = list(s)
    answer = ''
    # 반복문 내에서 단어 별 인덱스 역할을 할 변수
    num = 0
    for i in s:
        # 공백일 경우 새로운 문자가 시작된다고 가정하고 num을 초기화
        # 그 외의 경우 짝수 위치에 있으면 대문자로, 홀수 위치에 있으면 소문자로 변경하여 추가하고 index 증가
        if i == ' ':
            answer = answer + ' '
            num = 0
        elif num % 2 == 0:
            answer += i.upper()
            num += 1
        else:
            answer += i.lower()
            num += 1
    return answer
