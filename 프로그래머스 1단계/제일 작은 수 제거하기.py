# 유의사항: 기존 배열은 내버려두고 다른 곳에서 배열을 변수로 저장하고 싶다면 sorted(list)를 활용해보자
def solution(arr):
    answer = []
    arr2 = sorted(arr)
    s = arr2[0]
    arr.remove(s)
    answer = arr
    if len(arr) == 0:
        answer.append(-1)
    return answer
