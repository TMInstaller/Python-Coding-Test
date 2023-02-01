# 제발 return 값좀 잘 살펴볼 것
def solution(s):
    answer = True
    # p, y 의 대소문자를 따로 구별하지 않으므로 전부 소문자로 바꾸고 진행하였다
    s = list(s.lower())
    print(s)
    pcount = 0
    ycount = 0
    for i in s:
        if 'p' == i:
            pcount += 1
        elif 'y' == i:
            ycount += 1
    if pcount != ycount:
        answer = False

    return answer
