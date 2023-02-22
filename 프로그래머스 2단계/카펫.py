def solution(brown, yellow):
    # S = brown + yellow
    # 노란색의 면적 Y = (width-2) * (height-2)
    # 갈색 면적 B = S - Y
    answer = [0, 0]  # 가로, 세로
    S = brown + yellow
    # 갈색 면적으로 테두리를 만들 수 있는 경우를 구하면서 answer에 대입
    # 그 경우에서 Y공식을 대입했을 때 맞다면 정답으로 출력하기
    for width in range(S-1, 0, -1):
        if S % width != 0:
            continue
        height = S / width
        y = (width - 2) * (height - 2)
        b = S - y
        if brown == b and yellow == y:
            answer[0] = width
            answer[1] = height
            break
    return answer
