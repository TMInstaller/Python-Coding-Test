# 풀이 추가
def solution(lottos, win_nums):
    # 정답배열, 맞춘 숫자, 그려서 못보는 숫자를 담을 배열, 변수 선언
    answer = []
    count = 0
    draw = 0
    # 로또 당첨번호에서 비교해서 맞춘개수와 그린 숫자 개수 보기
    for i in lottos:
        if i in win_nums:
            count += 1
        elif i == 0:
            draw += 1
    # 최고 점수와 최소 점수 넣기
    score = [count + draw, count]
    # 1~5등과 낙첨을 구분 할 코드 작성
    for i in score:
        if i > 1:
            answer.append(7-i)
        else:
            answer.append(6)
    return answer
