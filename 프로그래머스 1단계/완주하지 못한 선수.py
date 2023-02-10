# 풀이 추가
# 해시 문제이며, hash()를 사용하라는 의도로 낸 듯 하다
# hash() = 각 값에 대해 중복되지 않는 정수형의 수를 반환해주는 메소드이다
# 따라서 고유한 값이 key값으로, list안에 들어있는 값이 value가 되어 dic형태로 반환된다
# 그렇기 때문에 모든 정수값을 하나의 변수에 합해준 뒤 완주자의 정수값의 합을 빼주면 완주하지 못한 선수만이 남는다
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for p in participant:
        dic[hash(p)] = p
        temp += int(hash(p))
    for c in completion:
        temp -= hash(c)
    answer = dic[temp]
    return answer
