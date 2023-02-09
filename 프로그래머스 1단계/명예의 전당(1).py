# 풀이 추가
def solution(k, score):
    # 명예의 전당 최하위 점수들을 받을 배열과 임시로 점수들을 하나하나씩 넣을 배열 선언
    answer = []
    lowNum = []
    # lowNum에 하나씩 추가하며 k개보다 적을 때에는 그 중 최솟값을, k개보다 많을 때에는 오름차순 정렬 후 -k번째를 배열에 넣도록 설정
    # 명예의 전당에는 오름차순 한 배열의 -k번째부터 점수가 등록되어있다
    for i in score:
        if len(lowNum) >= k:
            lowNum.append(i)
            lowNum.sort()
            answer.append(lowNum[-k])
        else:
            lowNum.append(i)
            answer.append(min(lowNum))
    return answer
