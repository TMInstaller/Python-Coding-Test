# 유의사항: index 반환할 때 주의할 것
def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer = answer+'*'
    answer = answer + phone_number[-4:]
    return answer
