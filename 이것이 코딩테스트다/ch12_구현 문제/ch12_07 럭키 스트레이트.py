# 현재 점수 N
n = list(map(int, input()))
headN = []
tailN = []
for i in range(len(n)//2):
    headN.append(n[i])
    tailN.append(n[(i+1)*-1])

if sum(headN) == sum(tailN):
    print('LUCKY')
else:
    print('READY')
