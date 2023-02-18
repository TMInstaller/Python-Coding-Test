# 이 문제는 기본 코드가 제공되므로 상기 링크를 통해 문제를 풀어야 합니다
# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    # 문자열이 입력되었을 때의 완전탐색을 이용한다 (문자열 길이가 1000 이하이기 때문)
    answer = len(s)
    # 1개 단위부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j: j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
