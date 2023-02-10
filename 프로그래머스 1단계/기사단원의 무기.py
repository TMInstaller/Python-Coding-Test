# 풀이 추가
def solution(number, limit, power):
    answer = 0
    knight = []
    divisor_knight = []

    # 기사번호 담기
    for i in range(number):
        knight.append(i+1)

    # 각 기사번호 별 약수 담기
    for k in knight:
        tmp = []
        for i in range(1, int(k**(1/2)) + 1):
            if k % i == 0:
                tmp.append(i)
                if ((i**2) != k):
                    tmp.append(k // i)
        divisor_knight.append(len(tmp))

    for d in divisor_knight:
        if d <= limit:
            answer += d
        else:
            answer += power

    return answer
