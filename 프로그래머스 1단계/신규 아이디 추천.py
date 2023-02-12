# 풀이 추가
def solution(new_id):
    answer = ''
    # 1. 모든 대문자 소문자로
    new_id = new_id.lower()
    # 2. 아이디의 조건에 맞지 않는 문자 걸러내기
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            answer += i
    # 3. 아이디 내의 모든 '..' '.'으로 바꾸기
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4. 아이디의 첫 글자와 끝 글자가 '.'인 지 확인하고 제거하기
    # 4+. 문자열 길이가 1이고 문자가 '.'이면 두 번째 if문에서 제거된다
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5. 아이디가 비어있을 경우 'a'를 넣는다
    if answer == '':
        answer = 'a'
    # 6. 아이디가 15자를 넘을 경우 15자를 넘는 문자를 제거한다
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7. 아이디 길이가 3자보다 작을경우 3자가 될 때까지 아이디의 마지막 문자를 붙여넣는다
    while len(answer) < 3:
        answer += answer[-1]
    return answer
