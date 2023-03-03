def solution(sides):
    answer = 1
    sides.sort()
    if sides[2] >= sides[1] + sides[0]:
        answer = 2
    return answer
