# 풀이 추가
def solution(board, moves):
    answer = 0
    # 바구니 배열로 선언
    basket = []
    # 움직인 위치에서 board 한 층 씩 살펴보며 0이 아니면 바구니에 담기
    for m in moves:
        for bo in board:
            if bo[m-1] != 0:
                basket.append(bo[m-1])
                bo[m-1] = 0
                break
    # 바구니에 담긴 전체 배열을 무한반복시키며 인형을 없앨 수 없을 때까지 반복
    # count를 통해 인형이 사라지지 않는다면 반복문을 끝내고 결과를 출력
    while True:
        count = 0
        for i in range(1, len(basket)):
            if basket[i] == basket[i-1]:
                answer += 2
                count += 1
                basket.pop(i)
                basket.pop(i-1)
                break
        if count == 0:
            break

    return answer
