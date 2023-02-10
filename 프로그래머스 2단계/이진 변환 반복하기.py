# 풀이 추가
def solution(s):
    answer = []
    # 2진 변환 횟수를 담을 변수와 제거한 0의 개수를 세는 변수 선언
    count = 0
    zero = 0

    # 반복문을 통해 다음 작업을 수행
    # 0을 세서 그 개수를 zero에 추가
    # 0을 모두 제거 후 남은 문자열의 길이를 2진 변환
    # 이 때, bin()을 사용할 경우 앞에 '0b'가 붙으므로 slicing 해준다
    # s가 1이 되면 반복을 멈추고 각 변수들을 answer에 담아 출력
    while s != '1':
        zero = zero + s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]

        count += 1
    answer = [count, zero]

    return answer
