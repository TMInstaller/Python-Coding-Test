# 풀이
def solution(s, n):
    answer = ''
    # a~z까지 적어두고 n값이 25까지 있으므로 뒤에 a~y까지 다시 쓰기
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy'
    # 대문자일 경우 소문자로 저장해두기 위한 변수 선언
    ss = ''
    # alphabet + n값을 출력하기 위한 index 담을 변수 선언
    aindex = 0
    for i in range(len(s)):
        # 공백일 경우 공백 추가 후 사이클 건너뛰기
        if s[i] == ' ':
            answer += ' '
            continue
        # 대문자일 경우 소문자로 바꿔주어 담아두는 작업
        if s[i].isupper():
            ss = s[i].lower()
        # 소문자인 상태에서 알파벳 안에 있을 경우 aindex에서 위치를 저장하고 n만큼 뒤로 밀고 answer에 추가
        # 소문자로 변경 된 상태에서 알파벳 안에 있을 경우 aindex에 위치를 저장하고 n만큼 뒤로 밀고 대문자로 바꿔서 answer에 추가
        if s[i] in alphabet:
            aindex = alphabet.index(s[i])
            answer += alphabet[aindex+n]
        elif ss in alphabet:
            aindex = alphabet.index(ss)
            answer += alphabet[aindex+n].upper()
        ss = ''
    return answer
