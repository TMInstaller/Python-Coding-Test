# 풀이 추가
def solution(n, words):
    # 정답의 첫 번째 인덱스에는 몇 번째 사람이 들어가야 하므로 %연산을 이용한다
    # 정답의 두 번째 인덱스에는 몇 번째 바퀴가 들어가야 하므로 //연산을 이용한다
    answer = []

    # 반복문을 통해 단어들을 쭉 돌린다
    for i in range(1, len(words)):
        # 지금까지 나왔던 단어가 한 번 더 나온다던가 끝말잇기가 올바르지 않은 단어로 진행될 경우
        # else 에서 변경되었을 지 모르는 answer을 한 번 초기화 시킨다
        # 그 후 순서와 바퀴를 정답에 집어넣고 반복문을 종료한다
        if words[i] in words[:i] or words[i-1][-1] != words[i][0]:
            answer = []
            answer.append((i % n) + 1)
            answer.append((i // n) + 1)
            break
        else:
            answer = [0, 0]

    return answer
