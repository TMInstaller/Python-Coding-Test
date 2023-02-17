# 1회 - 정답
# 볼링공의 개수 N, 공의 최대 무게 M
n, m = map(int, input().split())
# 각 볼링공의 무게 K
k = list(map(int, input().split()))
# 두 사람이 고른 볼링공의 무게가 같으면 count하지 않기
count = 0
for i in range(n):
    for j in range(i+1, n):
        if k[i] != k[j]:
            count += 1

print(count)
