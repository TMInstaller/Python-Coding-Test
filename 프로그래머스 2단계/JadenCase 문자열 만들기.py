# 유의사항 : list comprehension = [출력하고자 하는 것, for 변수 in 배열]
# 유의사항 2 : .capitalize() 첫 글자만 대문자로 변경
# 유의사항 3 : '기준 문자열'.join(배열명) = '기준 문자열'을 사이에 두고 합치기
def solution(s):
    s = s.lower()
    s = s.split(' ')
    s = [i.capitalize() for i in s]
    answer = ' '.join(s)
    return answer
