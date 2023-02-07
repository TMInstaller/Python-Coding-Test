# 풀이 추가
def solution(food):
    answer = ''
    # food[1]번부터 //2번씩 배열에 넣기
    # string으로 바꾸고 0을 뒤에 붙여넣기
    # 역순으로 변경 후 그대로 뒤에 붙여넣기
    for i in range(1, len(food)):
        answer += str(i) * (food[i]//2)
    answer += '0'
    for i in range(len(food)-1, 0, -1):
        answer += str(i) * (food[i]//2)
    return answer
