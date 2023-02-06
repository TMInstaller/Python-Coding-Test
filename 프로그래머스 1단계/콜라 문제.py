# 풀이 추가
def solution(a, b, n):
    # 일단 a로 n을 나눈 몫 * b를 answer에 더해둔다
    # n의 값을 (a로 나눈 몫 * b) + (a로 나눈 나머지)로 설정한다
    # 반복한다
    answer = 0
    while n >= a:
        answer += (n//a * b)
        n = n//a * b + n % a
    return answer
