# a = input()

# c = 0
# while c < len(a) // 2:
#     if a[0 + c] == a[len(a) - 1 - c]:
#         c += 1
#     else:
#         break
# if c == len(a) // 2:
#     print(True)
# else:
#     print(False)

# 회문이랑 앞으로 읽어도 뒤로 읽어도 똑같은 문자를 말한다.
# sos, level, ratator, nurse run(띄어쓰기 빼고) 등이 있다.
# 위 코드는 내가 직접 만들어본 회문일 경우 Ture를 출력해주는 코드이다

# word = input('단어를 입력하세요 : ')

# is_palindrome = True # 회문 판별값을 저장할 변수, 초기값 True
# for i in range(len(word) // 2): # 0부터 문자열 길이의 절반만큼 반복
#     if word[i] != word[-1 - i]: # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다를 경우,
#         is_palindrome = False # 회문이 아니므로 False를 변수에 할당
#         break
# print(is_palindrome)

# word = input('단어를 입력하세요 : ')
# print(word == word[::-1])

# 문자열을 뒤집어서 연산자로 확인하면 간단하게 회문을 구분하는 연산자를 만들 수 있다.

# word = input('단어를 입력하세요 : ')
# print(list(word) == list(reversed(word)))

# 문자열이 할당된 변수 word를 list함수로 리스트화 시킨 후 reversed함수로 뒤집어서 연산자로 회문을 구분하게 만들수도 있다.

# word = input('단어를 입력하세요 : ')
# print(word == ''.join(reversed(word)))

# reversed와 join을 융합하여 사용하면 뒤집어진 문자열을 반환시킬 수 있습니다.

# t = 'hello'
# for i in range(len(t) - 1):
#     print(t[i], t[i+1], sep='')

# 글자 N-gram 만들기란 문자열 시작부터 n개씩 출력해서 끝 글자가 나올때까지 출력하는 방식입니다.

# t = 'this is python script'
# w = t.split()
# for i in range(len(w) - 1):
#     print(w[i], w[i + 1])
# 단어 N-gram을 만들려면 문자열을 split 메소드를 이용하여 리스트화 시킨 후 글자 N-gram을 만들듯 만들어주면 됩니다.

# t = 'hello'
# two_gram = zip(t, t[1:])
# for i in two_gram:
#     print(i[0], i[1], sep='')

# zip(a, b) 시퀀스 자료형 a, b의 요소를 하나씩 꺼내서 튜플로 묶어서 짝을 이룬 자료로 만들어 줍니다.

# t = 'hello'
# tg = zip(*[t[i:] for i in range(2)])
# for i in tg:
#     print(i[0], i[1], sep='')

# zip과 리스트표현식을 이용해서 t, t[1:]....t[n:]을 같이 n이 클경우 짧게 축약하는 코드를 만들 수 있습니다.
# 단, zip함수 안 표현식 앞에 *이 붙는데 이것은 후에 리스트 언패킹이라는 스킬을 배우니 눈도장만 찍어둡니다.