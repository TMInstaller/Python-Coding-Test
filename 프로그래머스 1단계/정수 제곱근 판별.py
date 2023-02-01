# 문제상황: 기존의 모든 수를 살펴보며 제곱근을 판별하는 방식으로는 큰 수에서 시간 초과가 났기에 더 좋은 방법을 생각해 낸 풀이
# 반복문을 제거해서 최적의 시간을 도출 해내었다
def solution(n):
    # 기본 예외 값 추가
    answer = -1
    # 주어진 정수를 제곱근으로 만들어보기
    num = n**(1/2)
    # int형 일 경우 제곱근이므로 answer에 넣어 return
    if num == int(num):
        answer = num
    if answer != -1:
        answer = (answer+1)**2
    return answer
