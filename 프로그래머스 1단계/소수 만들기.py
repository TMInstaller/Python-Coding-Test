# 풀이 추가
def solution(nums):
    answer = 0
    # 3개의 수를 더해서 나온 값들을 저장하는 배열 생성
    # 이 때, 같은 값이 나와도 다른 경우의 수 이므로 중복제거를 하지 않는다
    num = []
    # 조합 반복문
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                num.append(nums[i]+nums[j]+nums[k])
    # 소수 판별 반복문, 소수가 맞다면 answer에 하나씩 추가한다
    for i in num:
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            answer += 1
    return answer
