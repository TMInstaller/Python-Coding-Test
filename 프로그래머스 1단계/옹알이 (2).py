# 풀이 추가
def solution(babbling):
    answer = 0
    pronounce = ['aya', 'ye', 'woo', 'ma']

    # babbling을 하나씩 가져와서
    for bab in babbling:
        # pronounce를 하나씩 비교해본다
        for pron in pronounce:
            # 반복되는 말이 아니라면
            if pron*2 not in bab:
                # babbling의 현재 값에서 발음을 공백으로 바꿔본다
                bab = bab.replace(pron, ' ')
        # 일련의 과정이 끝난 후 공백만 남으면 제대로 발음했다는 의미이므로 answer을 1 증가시킨다
        if len(bab.strip()) == 0:
            answer += 1

    return answer
