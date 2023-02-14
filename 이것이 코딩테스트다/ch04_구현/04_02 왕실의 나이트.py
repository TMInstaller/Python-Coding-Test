# 117p 답안 예시
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
# ord() = unicode를 정수형으로 바꾸어주는 메소드
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for s in steps:
    # 이동하고자 하는 위치 확인
    nRow = row + s[0]
    nCol = column + s[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if nRow < 1 or nRow > 8 or nCol < 1 or nCol > 8:
        continue
    result += 1

print(result)
