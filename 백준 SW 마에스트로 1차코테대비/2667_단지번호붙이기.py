N = int(input())

house = []
for i in range(N):
    house.append(list(map(int, input())))
# 단지의 건물 개수를 담을 변수
count = 0


def dfs(x, y):
    # count를 글로벌 변수로 두고 사용
    # 범위 안에 있다면 상하좌우를 탐색해가며 단지 건물을 지워나감
    # 지워나가는 횟수를 count하고 아래에서 단지 별로 끊어서 내보낸다
    global count
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if house[x][y] == 1:
        house[x][y] = 0
        count += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


# 단지 별 건물 개수를 담을 배열, count가 들어간다
house_group = []
for i in range(N):
    for j in range(N):
        # dfs가 한 차례 실행되고 그동안 count된 횟수 = 단지 별 건물 수
        if dfs(i, j) == True:
            house_group.append(count)
            count = 0
# 단지 수를 출력하고 건물 개수를 오름차순으로 출력
house_group.sort()
print(len(house_group))
for i in range(len(house_group)):
    print(house_group[i])
