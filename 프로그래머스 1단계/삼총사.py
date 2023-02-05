# 풀이 추가 : 1점짜리문제를...
def solution(number):
    answer = 0
    # 한 자리수 뒤로 밀어내며 모든 경우의 수를 구해봅니다. 이렇게 할 시 순서 상관없는 모든 경우의 수를 구해볼 수 있습니다
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer
