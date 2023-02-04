# 풀이
def solution(d, budget):
    answer = 0
    # d를 오름차순으로 정렬
    d.sort()
    # 지원해 주고 남은 예산과 지원해 준 팀을 반복해서 확인하기
    for i in range(len(d)):
        if d[i] > budget:
            break
        budget -= d[i]
        answer += 1
    return answer
