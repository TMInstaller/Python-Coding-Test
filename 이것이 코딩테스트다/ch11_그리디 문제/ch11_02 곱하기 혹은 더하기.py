# 1회 - 풀이보고 예외사항 추가
n = list(map(int, input()))
answer = 0
for i in n:
    if i == 0:
        continue
    if answer == 0:
        answer = i
    else:
        if i == 1:
            answer += 1
            continue
        answer *= i

print(answer)
