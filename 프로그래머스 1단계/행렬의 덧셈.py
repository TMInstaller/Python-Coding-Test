# 풀이: 2차 행렬끼리의 덧셈이다
# 둘이 같은 길이와 크기의 행렬이므로 길이값, 크기값만큼 반복문을 시작한다
# 둘이 같은 크기의 행렬이기에 각 위치별로 더해주고 반환 해준다
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1
