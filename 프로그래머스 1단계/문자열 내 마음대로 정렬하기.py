# 풀이 추가
def solution(strings, n):
    answer = []
    # 임시 답변을 저장할 배열
    sAnswer = []
    # n번째 index를 제일 앞에 붙여놓을 반복문
    for i in strings:
        sAnswer.append(i[n] + i)
    # 배열 알파벳순으로 정렬
    sAnswer.sort()
    # 정답에 붙여둔 알파벳 떼고 출력
    for s in sAnswer:
        answer.append(s[1:])
    return answer
