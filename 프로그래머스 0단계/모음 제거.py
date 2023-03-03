def solution(my_string):
    answer = ''
    vowel = 'aeiou'
    for s in my_string:
        if s in vowel:
            continue
        else:
            answer += s
    return answer
