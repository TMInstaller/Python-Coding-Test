# Python 자체의 최대 재귀 깊이가 달라질 수 있기에 1000회가 넘을 것으로 예상되면
# sys.setrecursionlimit(10**6)으로 10억회를 설정해서 recursion error을 피하도록 하자
import sys
sys.setrecursionlimit(10**6)

# 테스트 케이스 개수
T = int(input())

# 재귀를 이용한 상하좌우 DFS 블록탐색 함수


def dfs(xpos, ypos):
    if xpos >= N or xpos <= -1 or ypos >= M or ypos <= -1:
        return False

    if d[xpos][ypos] == 1:
        d[xpos][ypos] = 0
        dfs(xpos + 1, ypos)
        dfs(xpos - 1, ypos)
        dfs(xpos, ypos + 1)
        dfs(xpos, ypos - 1)
        return True

    return False


# 테스트 케이스 만큼 반복
for _ in range(T):
    M, N, K = map(int, input().split())
    d = [[0] * M for _ in range(N)]
    for i in range(K):
        # 여기서 주의할 점: y, x의 형태로 심어지므로 좌표값을 변경할 때 주의하자
        x, y = map(int, input().split())
        d[y][x] = 1
    result = 0
    # 2중 반복문으로 블록 개수 탐색
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result += 1
    print(result)
