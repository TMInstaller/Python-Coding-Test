# 유의사항: True, False 대소문자 구분 잘 하기
def solution(absolutes, signs):
    answer = 0
    for i, j in zip(absolutes, signs):
        if j == False:
            answer -= i
        else:
            answer += i
    return answer
