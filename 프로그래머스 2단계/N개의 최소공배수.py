def solution(arr):
    answer = 0
    for i in range(1, len(arr)):
        for j in range(arr[i], arr[i-1]*arr[i] + 1):
            if j % arr[i] == 0 and j % arr[i-1] == 0:
                arr[i] = j
                break
        answer = arr[i]
    return answer
