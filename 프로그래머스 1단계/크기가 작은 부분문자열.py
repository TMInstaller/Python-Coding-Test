# 풀이 추가
def solution(t, p):
    answer = 0
    num = []
    # p의 길이에 맞게 배열을 나눠두기 위한 반복문
    for i in range(len(t)-len(p)+1):
        num.append(t[i:i+len(p)])
    # 그 중에서 p보다 작은 수의 개수를 구하기 위한 반복문
    for j in num:
        if int(j) <= int(p):
            answer += 1

    return answer
