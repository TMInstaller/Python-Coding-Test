# 풀이 추가
def solution(array, commands):
    answer = []
    # 임시로 나눠놓은 숫자를 담을 배열 선언
    tmp = []
    # 각각의 케이스에 대하여
    # 숫자열 범위가 있다면 tmp에 담아두고 정렬한 다음 적정 위치의 숫자 뽑기
    # 숫자 단 하나만을 뽑는 경우 그 위치에 있는 숫자 집어넣기
    for i in commands:
        if i[0] != i[1]:
            tmp = array[(i[0]-1):(i[1])]
            tmp.sort()
            answer.append(tmp[i[2]-1])
        else:
            answer.append(array[i[0]-1])
    return answer
