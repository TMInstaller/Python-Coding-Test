# 풀이 추가
# 특징 : 가장 큰 수부터 차례대로 나열하는 것이 가장 큰 수의 조합이다
def solution(X, Y):
    answer = ''
    # 가장 큰 수인 9부터 겹치는 만큼 하나씩 answer에 추가하기
    for i in range(9, -1, -1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    # 예외처리 : 겹치는 부분이 없으면 추가 된 것들이 없을 것이므로 -1 반환
    # 예외처리 2 : answer 첫 글자가 0일 경우 뒤에도 다 0일 것이므로 0 반환
    if answer == '':
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        return answer
