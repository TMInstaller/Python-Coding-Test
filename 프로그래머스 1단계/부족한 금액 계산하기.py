# 유의사항: 조건 잘 읽기..
def solution(price, money, count):
    answer = -1
    for i in range(1, count+1):
        money -= (price*i)
    if money < 0:
        answer = -money
    else:
        answer = 0
    return answer
