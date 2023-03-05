# 키에 맞게 암호문을 해독하는 과정 수행
key = list(str(input()))
secret = str(input())

diction = []
keys = {}
for i in range(len(key)):
    di = ''
    for j in range(len(secret)//len(key)-1):
        di += secret[i*j+j]
    diction.append(di)
    keys[i] = key[i]

key.sort()
move = []
for i in range(len(key)):
    move.append(keys[key[i]])

print(diction, keys, key)
