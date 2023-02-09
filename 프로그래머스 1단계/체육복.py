# 풀이 추가
def solution(n, lost, reserve):
    # set을 이용해 각각이 겹치지 않도록 차집합을 구해둔다
    # 제한사항 중 여벌의 체육복이 있지만 분실한 사람이 따로 있기 때문이다
    reserve_set = set(reserve)-set(lost)
    lost_set = set(lost)-set(reserve)
    # 각 번호의 +-1을 보고 빌려줄 수 있다면 빌려주고 빌려 준 사람을 배열에서 제거한다
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    # 빌려줄 수 있는 여부를 모두 확인 한 후 못 빌린 사람의 수만 빼서 반환한다
    return n - len(lost_set)
