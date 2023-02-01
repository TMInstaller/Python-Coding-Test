# for문의 가변값과 고정값이 무엇인 지 정확히 인지하고 있을 것
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x * (i+1))
    return answer
