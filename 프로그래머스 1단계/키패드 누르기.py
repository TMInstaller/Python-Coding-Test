# 풀이 추가
def solution(numbers, hand):
    answer = ''
    # 키패드를 좌표로 변경
    num_pos = {1: [0, 0], 2: [0, 1], 3: [0, 2],
               4: [1, 0], 5: [1, 1], 6: [1, 2],
               7: [2, 0], 8: [2, 1], 9: [2, 2],
               '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    # 시작 위치 지정
    left_pos = num_pos['*']
    right_pos = num_pos['#']

    for n in numbers:
        now_pos = num_pos[n]
        # 무조건 왼손으로 누르는 버튼과 오른손으로 누르는 버튼 처리
        if n in [1, 4, 7]:
            answer += 'L'
            left_pos = now_pos
        elif n in [3, 6, 9]:
            answer += 'R'
            right_pos = now_pos
        # 중앙 숫자들에 대한 처리
        else:  # 2, 5, 8, 0
            left_center = 0
            right_center = 0
            # 거리 계산하기 ( 절대값 사용 )
            for lp, rp, np in zip(left_pos, right_pos, now_pos):
                left_center += abs(lp - np)
                right_center += abs(rp - np)
            # 가까운 손에 따른 처리
            if left_center < right_center:
                answer += 'L'
                left_pos = now_pos
            elif left_center > right_center:
                answer += 'R'
                right_pos = now_pos
            # 두 손의 거리가 같은 경우 처리
            else:
                # 왼손잡이 / 오른손잡이 처리
                if hand == 'left':
                    answer += 'L'
                    left_pos = now_pos
                else:
                    answer += 'R'
                    right_pos = now_pos

    return answer
