# 풀이 추가
# 연속된 숫자이기때문에 1234, 2345, 3456... 의 방법으로 가짓수를 구한다
# count에 담아두다가 그 값이 n과 일치하면 answer을 증가시키고, n을 넘어서면 효율성을 위해 반복을 중단시킨다
# 그렇게 n까지 가보면서 확인 해보고 나온 총 answer의 값을 반환한다
def solution(n):
    answer = 0
    for i in range(1, n+1):
        count = 0
        for j in range(i, n+1):
            count += j
            if count == n:
                answer += 1
                break
            elif count > n:
                break
    return answer
