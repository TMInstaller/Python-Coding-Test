def solution(n):
    ans = 0
    while n != 0:
        ans += n % 2
        n //= 2

    return ans
