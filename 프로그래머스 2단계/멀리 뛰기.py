def solution(n):
    # 한 번에 1칸 혹은 2칸 뛸 수 있음
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 3 5 8 13
    # 앞의 두 수를 합친 형태
    d = [0] * (n + 1)
    d[0] = 1
    d[1] = 2
    for i in range(2, n):
        d[i] = d[i-1] + d[i-2]
    return d[n-1] % 1234567
