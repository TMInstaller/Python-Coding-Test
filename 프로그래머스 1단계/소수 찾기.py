# 풀이 추가
# 이 문제는 일반적인 소수 알고리즘이 아닌 에라토스테네스의 체를 이용하여 풀어야 합니다
def solution(n):
    answer = 0
    # n의 길이를 가지고 있는 에라토스테네스의 체 생성
    num = [0] * (n+1)
    # 2부터 거르기 시작해서 소수별로 거르고 지우고 하는 반복문
    for i in range(2, n+1):
        if num[i] == 0:
            answer += 1
            for j in range(i, n+1, i):
                num[j] = 1

    return answer
