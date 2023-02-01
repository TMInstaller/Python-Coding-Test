# 유의사항: 별 것 아닌 것처럼 보이는 기능도 모두 넣는다 생각하고 풀 것
def solution(s):
    answer = True
    s = list(s)
    num = '0123456789'
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i in num:
                continue
            else:
                answer = False
                break
    else:
        return False
    return answer
