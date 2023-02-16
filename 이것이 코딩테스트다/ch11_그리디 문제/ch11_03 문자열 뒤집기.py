# 1회
# 0001100 -> 1회
# 1101010 -> 3회

n = list(map(int, input()))
tmp = 0
for i in range(1, len(n)):
    if n[i-1] != n[i]:
        tmp += 1

print(tmp - 1)
