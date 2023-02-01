# 유의사항: 웬만한 수 관련 반복문은 1부터 끝까지 돌릴 것
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
        print(answer)
    return answer
