# 풀이 추가
def solution(s):
    answer = []
    # list로 바꾸고 바꾼 각각의 알파벳에 대해 index의 차이를 이용해본다
    s = list(s)
    alpha = []
    aindex = []
    # list에서 처음 나오는 알파벳인지 확인하는 코드
    # 처음 나오는 알파벳이 아니라면 기존 알파벳과의 차이가 얼마나 나는 지 계산하는 코드
    for i in range(len(s)):
        if s[i] not in alpha:
            alpha.append(s[i])
            aindex.append(i)
            answer.append(-1)
        else:
            aindex.append(i)
            answer.append(i-aindex[alpha.index(s[i])])
            alpha[alpha.index(s[i])] = ''
            alpha.append(s[i])
    return answer
