# 풀이 추가
def solution(n, arr1, arr2):
    answer = []
    # 각각의 지도들을 한번에 2진수로 바꾸고
    # bin()을 사용하면 앞에 0b가 붙으므로 이를 슬라이싱 해 준 다음
    # 한 변의 길이가 n이므로 비어있는 앞 공간을 0으로 채워준다
    # 그 후 1을 #으로, 0을 공백으로 치환해서 정답 출력
    for i in range(n):
        # bin(a|b)를 하면 하나라도 1이 될 경우 1로 출력한다
        t = bin(arr1[i] | arr2[i])
        t = t[2:].zfill(n)
        t = t.replace('1', '#').replace('0', ' ')
        answer.append(t)
    return answer
