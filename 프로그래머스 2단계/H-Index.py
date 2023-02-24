def solution(citations):
    answer = 0
    # n편의 논문 중 h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용
    # 3논문은 3이상 인용된 논문 (자신포함) 3개 이상을 가지고 있어야 한다
    # 하지만 3보다 덜 인용된 논문이 (자신포함) 3개를 넘어서는 안된다
    # [0 0 3 4 5 6 7 8]

    citations.sort()
    for i in range(len(citations)):
        h_index = len(citations) - i
        if citations[i] >= h_index:
            answer = h_index
            break

    return answer
