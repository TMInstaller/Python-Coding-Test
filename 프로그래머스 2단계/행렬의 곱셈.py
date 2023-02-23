def solution(arr1, arr2):
    # 행렬곱 = arr1의
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(answer)):
        for j in range(len(answer[0])):
            sum = 0
            for k in range(len(arr2)):
                sum += arr1[i][k] * arr2[k][j]
            answer[i][j] = sum
    return answer
