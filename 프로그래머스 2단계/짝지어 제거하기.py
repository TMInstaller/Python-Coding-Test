def solution(s):
    if len(s) % 2 == 1:
        return 0  # 문자가 홀수개면 무조건 남는다.
    if len(s) == 2:  # 문자가 2개이고, 같은 문자라면 무조건 가능
        return 1 if s[0] == s[1] else 0

    stack = [s[0]]
    # stack에 s의 첫 값을 미리 넣어두고 확인하는 반복문
    # 2번 째 부터 하나씩 확인하면서 1, 2번째에 같은 것이 들어있으면 새로 추가하는 것이 아닌 이미 들어있는 것을 제거
    # 같은 것이 들어있지 않거나 배열이 비어있을 경우 삽입한다
    for v in s[1:]:
        if len(stack) > 0 and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)

    return 0 if len(stack) else 1
