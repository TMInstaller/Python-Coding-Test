# 풀이 추가
# try, except는 이런 문제처럼 테스트 케이스가 여러 개 들어가있지만 몇 개 들어간다고
# 명시되지 않은 테스트에서 사용할 수 있다 while로 감싸고 try: except EOFError: 을 활용해보자
while True:
    try:
        # 문자열 둘 입력받기
        s, t = map(str, input().split())
        count = 0
        answer = 'No'
        # Yes가 될 상황만 고려해본다
        # s와 t를 비교해보는 반복문, s에는 count를 통해 하나씩 증가시켜보면서 t하고 비교해본다
        # 다르다면 t의 그 다음 문자부터 비교해보는 느낌으로 반복한다
        for i in range(len(t)):
            if s[count] == t[i]:
                count += 1
            else:
                continue
            # count는 사이에 있는 문자가 달라도 끝까지 비교했을 때 길이가 같으므로 Yes에 충족된다
            if count == len(s):
                answer = 'Yes'
                break
        print(answer)
    except EOFError:
        break
