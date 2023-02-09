# 유의사항 : return값이 올바른 지 확인하기
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    B.reverse()
    for i in range(min(len(A), len(B))):
        answer += (A[i]*B[i])

    return answer
