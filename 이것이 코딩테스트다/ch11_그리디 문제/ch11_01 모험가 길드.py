# 1회
n = int(input())
scare = list(map(int, input().split()))
answer = 0
count = 0
INF = int(10**6 + 1)
d = [0] * (n + 1)
for i in range(len(scare)):
    d[i] += scare[i]
for i in range(max(scare)):
    if d[i] != 0:
        answer += 1
        count += d[i]
    if count > len(scare):
        answer -= 1
        break
print(d, answer)
