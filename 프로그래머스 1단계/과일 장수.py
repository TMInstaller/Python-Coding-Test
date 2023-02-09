# 풀이 추가
def solution(k, m, score):
    # answer에 나올 수 있는 과일상자의 가격들을 넣은 후 합산해서 반환
    answer = []
    # sorted를 이용해서 오름차순 정렬
    num = sorted(score)
    # 과일 박스에 담을 최대 개수만큼 상자가 나오므로 while문 사용
    while len(num) >= m:
        # 한 상자에 들어가는 과일의 가격들을 선언
        # 뒤에서부터 과일 상자에 들어가는 개수만큼 제외하면서 가격배열에 담기
        # 이 중에 0~m-1까지 들어가고, 뒤에 들어온 과일일 수록 과일 가격이 낮기에 가장 마지막의 과일 가격을 개당 가격으로 잡기
        # 그 과일의 값이 상자의 개당 과일 가격이므로 개수만큼 곱해서 정답배열에 넣기
        price = []
        for i in range(m):
            n = num.pop()
            price.append(n)
        answer.append(price[-1]*m)
    # 정답배열 총합 출력
    return sum(answer)
