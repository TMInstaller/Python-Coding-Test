# 풀이 추가
# 이 문제는 우리가 실제로 명함을 정리할 때 처럼 긴 변끼리 정렬 해주고 짧은 변끼리 정렬 해 준 다음
# 그 중에서도 가장 긴 변의 길이 끼리만 구해주면 되는 문제이다.
# 따라서 이를 떠올린다면 굉장히 간단하게 풀 수 있는 문제이다
def solution(sizes):
    answer = 0
    longLen = []
    shortLen = []
    for i in sizes:
        if i[0] > i[1]:
            longLen.append(i[0])
            shortLen.append(i[1])
        else:
            longLen.append(i[1])
            shortLen.append(i[0])
    answer = max(longLen) * max(shortLen)
    return answer
