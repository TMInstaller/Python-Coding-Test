# 풀이 추가
def solution(s):
    number = ['zero', 'one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine']
    # number 안에 있는 영단어가 s 안에 존재하면 그 단어를 number index로 바꾼다(숫자로 변환)
    for i in range(len(number)):
        if number[i] in s:
            s = s.replace(number[i], str(i))
    return int(s)
