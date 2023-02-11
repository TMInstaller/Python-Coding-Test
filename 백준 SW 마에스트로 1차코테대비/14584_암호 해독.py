# 접근방식이 잘못되어있었다
# 1번째 입력 문자열을 하나씩 뒤로 밀어버리면서 사전에 있는 단어와 하나라도 일치하는 지 확인한다
# 하나라도 일치한다면 이를 출력한다
secret = str(input())
N = int(input())
diction = []
for i in range(N):
    diction.append(str(input()))

alpha = 'abcdefghijklmnopqrstuvwxyza'
index = 0
answer = ''
while True:
    new_secret = ''
    for i in secret:
        index = alpha.find(i)
        new_secret += alpha[index + 1]
        secret = new_secret

    for d in diction:
        if d in secret:
            answer = secret

    if len(answer):
        break

print(answer)
