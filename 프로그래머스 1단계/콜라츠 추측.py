# 유의사항: 반복문은 조건이 false가 될 때 종료된다
def solution(num):
    count = 0
    while num != 1:
        if count > 500:
            count = -1
            break
        if num % 2 == 0:
            num = num//2
        else:
            num = num*3 + 1
        count += 1
    answer = count
    return answer
