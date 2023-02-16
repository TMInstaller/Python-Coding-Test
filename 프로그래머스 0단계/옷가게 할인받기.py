def solution(price):
    answer = price
    if answer >= 500000:
        price = price * 0.8
    elif answer >= 300000:
        price = price * 0.9
    elif answer >= 100000:
        price = price * 0.95
    return int(price)
