# 풀이 추가
def solution(n):
    # 3진법으로 바꾸고 저장하는 배열 생성
    nthree = []
    while n >= 3:
        nthree.append(n%3)
        n = n//3
    # 마지막 남은 n을 추가해서 3진수로 완성하고 뒤집기
    nthree.append(n)
    nthree.reverse()
    # 정답을 담을 변수
    answer = 0
    # 수들을 10진수로 변환하기 위한 반복문 추가
    for i in range(len(nthree)):
        answer += (nthree[i] * (3**i))
    return answer