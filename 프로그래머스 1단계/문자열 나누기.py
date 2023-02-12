# 풀이 추가
def solution(s):
    # count 할 배열 미리 생성, 처음에는 첫 번째 글자 저장
    # 두 번째와 세 번째에는 각각 s[0]과 동일하고, 다른 문자를 세는 자리이다
    answer = 0
    count = [s[0], 0, 0]
    # count에 저장된 변수들의 조건에 맞게 작성하고 문제에 나온 조건에 따라 마지막에 한 번 더 분리한다
    for i in range(len(s)-1):
        if count[0] == s[i]:
            count[1] += 1
        else:
            count[2] += 1
        if count[1] == count[2]:
            answer += 1
            count = [s[i+1], 0, 0]
    answer += 1
    return answer
