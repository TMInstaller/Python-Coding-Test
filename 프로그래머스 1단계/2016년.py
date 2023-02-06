# 풀이 추가
def solution(a, b):
    answer = ''
    # 1월 1일은 금요일이고 그로부터 정확히 일 주일 후는 목요일이므로 목~수까지의 배열 생성
    Day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    # 윤년이기에 각 월별 일수를 나타내는 배열 추가
    Month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 총 일수 구하는 변수
    day = 0
    # ex) 5월일 경우 4월까지만 일 수를 더하면 되므로 a-1까지를 범위로 지정
    for i in range(a-1):
        day += Month[i]
    # 월을 더했으니, 일수를 더한다
    day += b
    # 7로 나눈 나머지 = 요일이므로 이를 반환한다
    answer = Day[day % 7]
    return answer
