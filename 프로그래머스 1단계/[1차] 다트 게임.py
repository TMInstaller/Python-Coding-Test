# 풀이 추가
def solution(dartResult):
    cal = []
    # S, D, T일 때  제곱해 줄 숫자를 dict형태에 담아두기
    SDT = {'S': 1, 'D': 2, 'T': 3}
    # 10을 문자 N으로 바꿔서 한글자씩 판별할 수 있도록 하기
    dr = dartResult.replace('10', 'N')
    # 총 4가지 경우의 수로 나누어서 판별하기
    # 1. 현재 위치에 숫자이거나 10을 변경한 N이 온다면 10 또는 i를 cal 에 넣기
    # 2. 현재 위치에 점수에 영향을 주는 SDT가 온다면 이전에 넣었던 수를 뽑아 연산하고 다시 집어 넣기
    # 3. 현재 위치에 *이 온다면 이전 수를 빼고 그 이전 점수가 존재하면 이를 2배하고 방금 뺀 점수를 2배해서 집어넣기
    # 4. 현재 위치에 #이 온다면 바로 이전 점수에 -1을 곱해주기
    for i in dr:
        if i.isdigit() or i == 'N':
            cal.append(10 if i == 'N' else int(i))
        elif i in ('S', 'D', 'T'):
            num = cal.pop()
            cal.append(num**SDT[i])
        elif i == '*':
            num = cal.pop()
            if len(cal):
                cal[-1] *= 2
            cal.append(num*2)
        elif i == '#':
            cal[-1] *= -1
    # 숫자 배열 합산해서 반환하기
    return sum(cal)
