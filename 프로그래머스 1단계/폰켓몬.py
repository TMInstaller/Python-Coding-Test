# 풀이 추가
def solution(nums):
    answer = 0
    # 선택하려는 폰켓몬의 수를 담아두는 변수
    n = len(nums)//2
    # 폰켓몬 수의 최댓값을 뽑기 위해 중복을 제거
    nums = list(set(nums))
    # 선택하려는 폰켓몬 수 보다 존재하는 폰켓몬 종류가 작을 때랑 아닐 때를 나눠 결과를 반환
    if len(nums) < n:
        answer = len(nums)
    else:
        answer = n
    return answer
