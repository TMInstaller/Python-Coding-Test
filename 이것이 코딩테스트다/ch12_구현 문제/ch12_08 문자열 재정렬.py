# 문자열 S
s = str(input())
alpha = []
num = []
for i in s:
    if i.isalpha():
        alpha.append(i)
    else:
        num.append(int(i))

alpha.sort()
num.sort()
print(('').join(alpha), end='')
print(sum(num))
