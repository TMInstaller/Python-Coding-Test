# 풀이 추가
def solution(numbers):
    answer = []
    # 예외처리를 위한 변수 num 추가
    num = 0
    # 2개의 경우의 수를 뽑는 반복문(2중)
    # 만약 이미 리스트에 들어가있다면 더한 숫자 추가하지 않기
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            num = numbers[i] + numbers[j]
            if num in answer:
                continue
            answer.append(num)
    answer.sort()
    return answer
