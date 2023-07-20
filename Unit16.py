# for 변수 in range(횟수):
#     반복할 코드

# for문과 range함수를 이용해서 코드를 원하는만큼 반복하도록 만들 수 있다.

# for i in range(100):
#     print('Hello, world!')

# range(100)에는 1~100까지 숫자가 있습니다.
# range(100)숫자를 하나씩 꺼내서 변수 i에 할당하고 할당할 때 마다 코드를 실행합니다.

# for i in range(5, 12):
#     print('Hello, world!', i)
# for i in range(0, 10, 2):
#     print('Hello, world!', i)
# for i in range(10, 0, -1):
#     print('Hello, world!', i)
# for i in reversed(range(10)):
#     print('Hello, world!')

# for문과 range를 사용할 때도 (x, y, z)로 시작, 끝, 증감폭을 지정할 수 있으며, y의 값은 포함되지 않습니다.
# 시작과 끝을 뒤집어놓고 증감폭을 음수로 두면 작아지는 순서로 반복할 수 있습니다.
# reversed함수를 사용해도 증감폭을 음수로 지정한 것과 같은 결과를 얻을 수 있습니다.

# count = int(input('반복할 횟수를 입력하세요 : '))

# for i in range(count):
#     print('Hello, world!', i)

# input으로 입력 값을 받아서 range 함수에 넣어주면 입력값으로 반복하는 코드를 만들 수 있습니다.

# a = [10, 20, 30, 40, 50]

# for i in a:
#     print(i)
# print(a)

# b = 'a', 'b', 'c', 'd', 'e'

# for j in b:
#     print(j)
# print(b)

# c = {'x' : 100, 'y' : 200, 'z' : 300}

# for k in c:
#     print(k)
# print(c)

# for letter in 'Python\n':
#     print(letter, end='')

# for letter2 in reversed('Python'):
#     print(letter2, end='')

# 시퀸스 자료형도 for문을 이용하여 하나씩 꺼내올 수 있습니다.
# 문자형 자료도 하나씩 꺼내올 수 있고 reversed를 이용해 거꾸로 꺼내올 수도 있습니다.
# for문은 원칙적으로 꺼내와도 시퀸스 자료의 원본은 바꾸지 않고 꺼내옵니다.
