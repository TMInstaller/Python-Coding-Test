def check(a, b):
    result = 0
    while True:
        a = a//2 + a % 2
        b = b//2 + b % 2
        result += 1
        if a == b:
            break
    return result


def solution(n, a, b):
    answer = check(a, b)
    return answer
