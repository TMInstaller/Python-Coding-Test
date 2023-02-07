# 풀이 추가
def solution(answers):
    answer = []
    # 시험의 정답은 answers에 들어있습니다
    # 각 수포자들이 찍는 패턴을 answers의 길이에 맞게 각각 배열로 세팅
    first = [1, 2, 3, 4, 5] * (len(answers)//5 + 1)
    second = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8 + 1)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)
    # 수포자들의 점수를 나타낼 변수
    firstA = 0
    secondA = 0
    thirdA = 0
    # 최대 점수를 담을 변수
    mScore = 0
    # 가장 높은 점수를 받은 학생들을 담을 배열
    score = []

    # 채점하는 반복문
    for i in range(len(answers)):
        if answers[i] == first[i]:
            firstA += 1
        if answers[i] == second[i]:
            secondA += 1
        if answers[i] == third[i]:
            thirdA += 1
    # 점수를 answer에 담아둡니다
    answer.append(firstA)
    answer.append(secondA)
    answer.append(thirdA)
    # 이 중에 최대 점수를 알아봅니다
    mScore = max(answer)
    # 1~3번 학생까지만 있으므로 다음과 같이 작성하고 학생의 점수가 최대 점수이면 score에 집어넣습니다
    # 오름차순 정렬이 필요 없도록 range를 지정하고 i+1을 넣는 방법으로 작성했습니다
    for i in range(3):
        if answer[i] == mScore:
            score.append(i+1)

    return score
