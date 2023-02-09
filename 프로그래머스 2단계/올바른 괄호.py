# 풀이 추가 : 스택 문제
def solution(s):
    # 스택 추가
    stack = []
    # 반복문을 통해 괄호가 올바른 지 확인해보기
    # '('일 때 스택에 추가 하기
    # ')'일 때 스택에 값이 존재하면 존재한 값을 빼서 () 완성
    # 그 외의 상황( ')'임에도 불구하고 스택이 비어있을 경우)에서 예외처리
    for i in s:
        if i == '(':
            stack.append(i)
        elif len(stack) and i == ')':
            stack.pop()
        else:
            return False
    # ()가 제대로 된 쌍을 이룰 경우 stack에는 아무런 값이 없을 것이기에 예외처리하여 반환
    return False if len(stack) else True
