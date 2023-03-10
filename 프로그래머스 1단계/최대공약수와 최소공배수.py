# 유의사항: range 역순정렬일 때 1까지 내려가도록 하려면 0까지 세팅해두자
def solution(n, m):
    answer = []
    for i in range(min(n, m)+1, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer
