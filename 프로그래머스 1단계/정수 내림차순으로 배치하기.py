# 유의사항: return값에 제대로 된 값이 들어가 있는 지 확인하기
def solution(n):
    answer = 0
    n = list(str(n))
    n.sort()
    n.reverse()
    print(n)
    answer = ''.join(n)
    return int(answer)
