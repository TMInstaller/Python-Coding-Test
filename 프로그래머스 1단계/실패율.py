# 풀이 추가
# 각 스테이지 별 실패율 구하기 => 실패율을 내림차순으로 스테이지 정렬하기
# dictionary자료형으로 실패율 만들고 dict정렬
def solution(N, stages):
    # 스테이지와 스테이지의 실패율을 담기 위해 두 개의 키 값을
    failure_rate = {}
    stages_len = len(stages)
    # 스테이지 길이를 줄여가며 failure_rate에 스테이지 별 실패율을 구하는 로직
    for i in range(1, N+1):
        if stages_len != 0:
            stage_count = stages.count(i)
            failure_rate[i] = stage_count/stages_len
            stages_len -= stage_count
        else:
            failure_rate[i] = 0
    # sorted는 sort와 다르게 원본을 변환시키지 않고 결과를 반환한다
    # 그리고 sorted 내부의 key=lambda 는 오름차순 정렬을 뜻하며, 여기에 reverse를 True로 두면 내림차순으로 만들 수 있다
    # 마치 sort()를 한 이후 reverse()를 써서 내림차순을 만들어주는 것과 같다
    answer = sorted(failure_rate.keys(),
                    key=lambda key: failure_rate[key], reverse=True)
    return answer
